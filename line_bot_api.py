# 載入LineBot所需的套件
from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler, exceptions)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('RAwLYo3oZVIR84NQ/a//R0FFmtzS4kkuty8tL7fkAsc6hEjUk48q0JtbpPlX8mr9cDyYZk0NvTToTIkhx6mRbVyeT7s/dvNl1vKKxmNhX3pmiKwFqlx8q0H51r4Wzri0ZWgWQaBaKi0Z0wvOqOw0kQdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('930c96dd10e22be503722d4d486a507d')