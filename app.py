# 載入LineBot所需的套件
from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler, exceptions)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

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
    # 自動回覆相同訊息
    # message = TextSendMessage(text=event.message.text)
    # line_bot_api.reply_message(event.reply_token, message)

    # 自己設定回覆訊息
    emoji = [
            {
                "index": 5,
                "productId": "5ac2280f031a6752fb806d65",
                "emojiId": "005"
            },
            {
                "index": 17,
                "productId": "5ac2280f031a6752fb806d65",
                "emojiId": "005"
            }
    ]

    text_message = TextSendMessage(text='''$ Master Finance $
HiHi 歡迎成為一起賺大錢的夥伴！
我是你的賺錢好夥伴
                                
- 這裡有股票 匯率資訊哦~
- 直接點選下方圖中選單功能
                                   
- 期待你的光臨！''', emojis = emoji)
    
    sticker_message = StickerSendMessag(
        package_id = '8522',
        sticker_id ='16581271'
    )
    line_bot_api.reply_message(
        event.reply_token,
        [text_message, sticker_message])
                                   

if __name__ == "__main__":
    app.run()