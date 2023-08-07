from line_bot_api import *
from events.basic import *
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
    messages_text = str(event.message.text).lower()
    
    if messages_text == '@使用說明':
        about_us_event(event)
        Usage(event)
     
    
      
if __name__ == "__main__":
    app.run()