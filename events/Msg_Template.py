from line_bot_api import *



def stock_reply_other(stockNumber):
    content_text = "請點選下列按鈕獲得資訊"
    text_message =  TextSendMessage(
                                    text = content_text,
                                    quick_reply=QuickReply(
                                        items = [
                                            QuickReplyButton(
                                                action = MessageAction(
                                                    label = "股票清單",
                                                    text = "股票清單"
                                                )
                                            ),
                                            QuickReplyButton(
                                                action = MessageAction(
                                                    label = "股價提醒",
                                                    text = "股價提醒"
                                            )
                                            ),
                                            QuickReplyButton(
                                                action = MessageAction(
                                                    label = "關閉提醒",
                                                    text = "關閉提醒"
                                                )
                                            )
                                        ]
                                    ))  
    return text_message

# 幣別種類Button
def show_Button():
    flex_message = FlexSendMessage(
            alt_text="幣別種類",
            contents={
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "  幣別種類  (  ⚯̱̈᷄  )",
                            "weight": "bold",
                            "size": "xl",
                            "color": "#F1C93B",
                            "align": "center"
                        }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "美金",
                                "text": "查詢匯率USD"
                                },
                                "gravity": "center",
                                "color": "#65451F",
                                "margin": "sm",
                                "style": "primary"
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "日圓",
                                "text": "查詢匯率JPY"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#65451F",
                                "margin": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "港幣",
                                "text": "查詢匯率HKD"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#65451F",
                                "margin": "sm"
                            }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "md",
                            "color": "#FBD85D"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "英鎊",
                                "text": "查詢匯率GBP"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#65451F",
                                "margin": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "澳幣",
                                "text": "查詢匯率AUD"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#65451F",
                                "margin": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "加幣",
                                "text": "查詢匯率CAD"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#65451F",
                                "margin": "sm"
                            }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "md",
                            "color": "#FBD85D"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "法郎",
                                "text": "查詢匯率CHF"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#65451F",
                                "margin": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "新加坡",
                                "text": "查詢匯率SGD"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#65451F",
                                "margin": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "南非幣",
                                "text": "查詢匯率ZAR"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#65451F",
                                "margin": "sm"
                            }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "md",
                            "color": "#FBD85D"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "瑞典幣",
                                "text": "查詢匯率SEK"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#65451F",
                                "margin": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "泰幣",
                                "text": "查詢匯率THB"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#65451F",
                                "margin": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "菲比索",
                                "text": "查詢匯率PHP"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#65451F",
                                "margin": "sm"
                            }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "md",
                            "color": "#FBD85D"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "印尼幣",
                                "text": "查詢匯率IDR"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#65451F",
                                "margin": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "韓元",
                                "text": "查詢匯率KRW"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#65451F",
                                "margin": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "馬來幣",
                                "text": "查詢匯率MYR"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#65451F",
                                "margin": "sm"
                            }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "md",
                            "color": "#FBD85D"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "越南盾",
                                "text": "查詢匯率VND"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#65451F",
                                "margin": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "人民幣",
                                "text": "查詢匯率CNY"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#65451F",
                                "margin": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "紐元",
                                "text": "查詢匯率NZD"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#65451F",
                                "margin": "sm"
                            }
                            ]
                        }
                        ]
                    },
                    "styles": {
                        "body": {
                        "backgroundColor": "#1A5D1A"
                        },
                        "footer": {
                        "backgroundColor": "#FBD85D"
                        }
                    }
                    }             
    )
    return flex_message