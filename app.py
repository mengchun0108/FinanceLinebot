# 載入LineBot所需的套件
from line_bot_api import *
from events.basic import *
from events.oil import *
from events.EXRate import *
from events.Msg_Template import *
from model.mongodb import *
import re
import twstock
import datetime
import asyncio

app = Flask(__name__)

# 抓使用者設定他關心的股票
def cache_users_stock():
    db = constructor_stock()
    nameList = db.list_collection_names()
    users = []
    for i in range(len(nameList)):
        collect = db[nameList[i]]
        cel = list(collect.find({"tag":'stock'}))
        users.append(cel)
    return users

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('RAwLYo3oZVIR84NQ/a//R0FFmtzS4kkuty8tL7fkAsc6hEjUk48q0JtbpPlX8mr9cDyYZk0NvTToTIkhx6mRbVyeT7s/dvNl1vKKxmNhX3pmiKwFqlx8q0H51r4Wzri0ZWgWQaBaKi0Z0wvOqOw0kQdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('930c96dd10e22be503722d4d486a507d')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    profile = line_bot_api.get_profile(event.source.user_id)
    uid = profile.user_id
    message_text = str(event.message.text).lower()
    msg = str(event.message.text).upper().strip()
    # 使用者輸入的內容
    emsg = event.message.text
    user_name = profile.display_name #使用者名稱

    ############################## 使用說明 選單 基德 油價查詢 ##############################
    if message_text == '@使用說明':
        about_us_event(event)
        Usage(event)

    if event.message.text == "@基德":
        buttons_template = TemplateSendMessage(
            alt_text = '你已得到基德的幫助',
            template=ButtonsTemplate(
                title='選擇服務',
                text='請選擇',
                thumbnail_image_url='https://imgur.com/mBwctnk.jpg',
                actions=[
                    MessageTemplateAction(
                        label="油價查詢",
                        text = '想知道油價'
                    ),
                    MessageTemplateAction(
                        label="匯率換算",
                        text = 
"""請輸入換匯(換前幣別)/(換後幣別)/(金額)
    ex : 換匯USD/TWD/100
"""
                    ),
                    MessageTemplateAction(
                        label="股票清單查詢",
                        text = '股票清單',
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)

    if event.message.text == '想知道油價':
        content = oil_price()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content)

        )
    ############################## 股票區 ##############################
    if event.message.text == "股價查詢":
        line_bot_api.push_message(uid, TextSendMessage("請輸入#股票代號"))
        # 用push_message方式回覆話語

    # 股價查詢
    if re.match("股票資訊", msg):
        btn_msg = stock_reply_other(msg)
        line_bot_api.push_message(uid, btn_msg)
        return 0
    
    # if re.match("想知道股價[0-9]", msg):
    #     msg = msg[5:]
    #     btn_msg = stock_reply_other(msg)
    #     line_bot_api.push_message(uid, btn_msg)
    #     return 0
    
    # 新增使用者關注的股票到mongodb
    if re.match('關注[0-9]{4}', msg):
        # 使用者新增股票質股票清單
        stockNumber = msg[2:6]
        line_bot_api.push_message(uid, TextSendMessage("加入股票代碼"+stockNumber))
        realtime_info = twstock.realtime.get(stockNumber)['realtime']
        stock_name = twstock.realtime.get(stockNumber)['info']['name'] + "（" + stockNumber + "）"
        now_price = f"{realtime_info['latest_trade_price'][:5]}"
        target_price = msg.split()[1][7:] if len(msg.split()[1]) > 7 else "NO"
        content = write_my_stock(uid, user_name, stock_name, now_price, target_price)
        line_bot_api.push_message(uid, TextSendMessage(content))
    # else:
    #     content = write_my_stock(uid, user_name, "未設定", "未設定")
    #     line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    
    # 查詢股票篩選條件清單
    if re.match('股票清單', msg):
        line_bot_api.push_message(uid, TextSendMessage('稍等一下，股票清單查詢中...'))
        content = show_stock_setting(user_name, uid)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    
    # 刪除存在資料庫裡的股票
    if re.match('刪除[0-9]{4}', msg):
        content = delete_my_stock(user_name, msg[2:])
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    
    # 清空存在資料庫裡的股票
    if re.match('清空股票', msg):
        content = delete_my_allstock(user_name, uid)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0

    # 查詢股票資訊
    if re.match('#', msg):
        line_bot_api.push_message(uid, TextSendMessage('稍等一下，股票查詢中...'))
        text = msg[1:]
        realtime_data = twstock.realtime.get(text)
        realtime_info = realtime_data['realtime']
        stock_info = realtime_data['info']
        past = twstock.Stock(text)

        now = f"{realtime_info['latest_trade_price'][:5]}"
        time = stock_info['time'].replace('-', '.').replace(stock_info['time'][11:13], str(int(stock_info['time'][11:13]) + 8))

        hour = int(time[11:13])
        before = past.price[-1] if 8 < hour < 14 else past.price[-2]
        increase = round(((float(now) - float(before)) / float(before)) * 100, 2)

        content = f"{stock_info['name']}（{stock_info['code']}）\n"
        content += "-------------\n"
        content += f"現價: {now}\n"
        content += f"漲跌: {round(float(now) - float(before), 2)}（{increase} %）\n"
        content += f"更新時間：\n{time}"

        line_bot_api.push_message(uid, TextSendMessage(content))

    #  五檔 - 未開發功能
    # if re.match('[0-9]{4}五檔', msg):
    #     line_bot_api.push_message(uid, TextSendMessage('稍等一下，五檔查詢中...'))
    #     text = emsg[:5]
    #     stock = twstock.realtime.get(text)

    if re.match('了解[0-9]{4}', msg):
        line_bot_api.push_message(uid, TextSendMessage('稍等一下，其他資訊查詢中...'))
        text = msg[2:6]

        realtime_info = twstock.realtime.get(text)['realtime']
        stock_info = twstock.realtime.get(text)['info']
        now = f"{realtime_info['latest_trade_price'][:5]}"
        open_price = f"{realtime_info['open'][:5]}"

        content = f"{stock_info['name']}（{stock_info['code']}）\n"
        content += "-------------\n"
        content += f"現價: {now}\n"
        content += f"開盤: {open_price}\n"
        content += f"最高: {realtime_info['high'][:5]}\n最低: {realtime_info['low'][:5]}\n"
        content += f"量: {realtime_info['accumulate_trade_volume']}"

        line_bot_api.push_message(uid, TextSendMessage(content))
        
    ############################## 匯率區 ##############################
    if re.match('幣別種類',emsg):
        message = show_Button()
        line_bot_api.reply_message(event.reply_token, message)

    if re.match('查詢匯率[A-Z]{3}', msg):
        msg = msg[4:]
        content = showCurrency(msg)
        line_bot_api.push_message(uid, TextSendMessage(content))

    if re.match('換匯[A-Z]{3}/[A-Z]{3}',msg):
        line_bot_api.push_message(uid, TextSendMessage("基德將為您做外匯計算"))
        content = main(msg)
        line_bot_api.push_message(uid, TextSendMessage(content))

    ############################## 股票提醒區 ##############################
    async def process_stock_alert(uid, stock, operator, target_price):
        try:
            loop = asyncio.get_event_loop()
            stock_info = await loop.run_in_executor(None, twstock.realtime.get, stock)
            realtime_info = float(stock_info['realtime']['latest_trade_price'])

            if operator == ">" and realtime_info > target_price:
                return f"{stock}賣光光賺大發！"

            elif operator == "<" and realtime_info < target_price:
                return f"{stock}問就是ALL IN！"

            elif operator == "=" and realtime_info == target_price:
                return f"{stock}到設定的價錢了快去看看！"

            else:
                return f"{stock}讓子彈再飛一會！"

        except Exception as e:
            return str(e)

    async def handle_stock_alert(uid, msg):
        if re.match("股價提醒", msg):
            db = constructor_stock()
            collect = db[user_name]
            dataList = list(collect.find({"userID": uid}))
            alerts = []

            for user_data in dataList:
                for stock_data in user_data:
                    stock_symbol = stock_data['favorite_stock'][-5:-1]
                    operator = stock_data['price'][0:1]
                    target_price = float(stock_data['price'][1:])
                    alert_message = await process_stock_alert(uid, stock_symbol, operator, target_price)
                    alerts.append(alert_message)

            if alerts:
                alert_message = "\n".join(alerts)
                line_bot_api.push_message(uid, TextSendMessage(text=alert_message))

    # 在主程式中執行非同步操作
    asyncio.run(handle_stock_alert(uid, msg))


@handler.add(FollowEvent)
def handle_follow(event):
    welcome_msg = '''HiHi 歡迎成為基德的夥伴！
                                
- 這裡有股票和匯率資訊哦
- 直接點選下方圖中選單功能
                                   
期待你的使用！'''
                                  
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=welcome_msg))

@handler.add(UnfollowEvent)
def handle_unfollow(event):
    print(event)

if __name__ == "__main__":
    app.run()