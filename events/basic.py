from line_bot_api import *

def about_us_event(event):
    # 自動回覆相同訊息
    # message = TextSendMessage(text=event.message.text)
    # line_bot_api.reply_message(event.reply_token, message)
    
    # 自己設定回覆訊息
    emoji = [
            {
                "index": 0,
                "productId": "5ac2280f031a6752fb806d65",
                "emojiID": "005"
            },
            {
                "index": 17,
                "productId": "5ac2280f031a6752fb806d65",
                "emojiID": "005"
            }
    ]

    text_message = TextSendMessage(text='''$ Master Finance $
HiHi 歡迎成為一起賺大錢的夥伴！
我是你的賺錢好夥伴
                                
- 這裡有股票 匯率資訊哦~
- 直接點選下方圖中選單功能
                                   
- 期待你的光臨！''', emojis = emoji)
    
    sticker_message = StickerSendMessage(
        package_id = '11539',
        sticker_id ='52114118'
    )
    line_bot_api.reply_message(
        event.reply_token,
        [text_message, sticker_message])