from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler, exceptions)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

app = Flask(__name__)

line_bot_api = LineBotApi('iMv8xguByzNjw1Iqz5dLPngS4mjjccdp6aF9dqdZBlSFMMKimZlb3UWH/l6XOId1QAatB9yE6kZR8qzh+onhKRBEkuwlRk/y92KcMIx1hkmZZiKdMH62dhl1HCrsRp864O8+ViYBYB2q5at+8E07swdB04t89/1O/w1cDnyilFU=')

handler = WebhookHandler('6e206be78064b105252cbfba09d43d27')

#監聽
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
        
    return 'OK'

#處理
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    emoji = [
        {
            "index" : 0,
            "productId": "5ac1bfd5040ab15980c9b435",
            "emojiId": "002"
        },
        {
            "index" : 2,
            "productId": "5ac1bfd5040ab15980c9b435",
            "emojiId": "002"
        }
    ]
    
    text_message = TextSendMessage(text='''$ $
Hello!
很高興認識你
需要甚麼幫助呢
''', emojis=emoji)
    # message = TextMessage(text=event.message.text)
    # line_bot_api.reply_message(event.reply_token, message)
    
    sticker_message = StickerMessage(
        package_id='11538',
        sticker_id='51626494'
    )
    line_bot_api.reply_message(
        event.reply_token,
        [text_message, sticker_message]
    )
    
if __name__ == "__main__":
    app.run()