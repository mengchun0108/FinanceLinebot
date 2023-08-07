# 載入LineBot所需的套件
from line_bot_api import *
from events.basic import *
from events.oil import *

app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('y183jnCciIWryNOI+kTjMm80wyo/KStYQCOLMlqrz4UZ62jOrdkaKMZ/N51MWbMfeqPB6pLdVbTxBim+pn6HExanDVsx7N994f0uOPVrVE/iBJiwBCWexTrbmIFrf5P3CG8LbKBseyKInUlkvynGgwdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('b0d867b52ea2085d294fbf521e2119d6')

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
    message_text = str(event.message.text).lower()
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
                        text = '油價查詢'
                    ),
                    MessageTemplateAction(
                        label="匯率查詢",
                        text = '匯率查詢'
                    ),
                    MessageTemplateAction(
                        label="股價查詢",
                        text = '股價查詢'
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

@handler.add(FloowEvent)
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