from line_bot_api import *
from events.basic import *
from events.oil import *

app = Flask(__name__)

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
    profile = line_bot_api.get_profile(event.source.user_id)
    uid = profile.user_id
    messages_text = str(event.message.text).lower()
    
    
    ######## 適用說明 選單 油價查詢
    if messages_text == '@使用說明':
        about_us_event(event)
        Usage(event)
     
    if event.message.text == "油價查詢":
        content = oil_price()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
    ########## 股票
    if event.message.text == "股價查詢":
        line_bot_api.push_message(uid, TextSendMessage("請輸入#加股票代號"))
    
@handler.add(FollowEvent)
def handler_follow(event):
    welcome_msg = '''Hello!
很高興認識你
這裡有股市、匯率等資訊
還需要其他幫助嗎?'''

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=welcome_msg))
    
@handler.add(UnfollowEvent)
def handle_unfollow(event):
    print(event)

      
if __name__ == "__main__":
    app.run()