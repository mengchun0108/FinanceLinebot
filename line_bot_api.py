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