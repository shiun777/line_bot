from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler, exceptions)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

app = Flask(__name__)

line_bot_api = LineBotApi('iMv8xguByzNjw1Iqz5dLPngS4mjjccdp6aF9dqdZBlSFMMKimZlb3UWH/l6XOId1QAatB9yE6kZR8qzh+onhKRBEkuwlRk/y92KcMIx1hkmZZiKdMH62dhl1HCrsRp864O8+ViYBYB2q5at+8E07swdB04t89/1O/w1cDnyilFU=')

handler = WebhookHandler('6e206be78064b105252cbfba09d43d27')