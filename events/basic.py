from line_bot_api import *

def about_us_event(event):
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
這裡有股市、匯率等資訊
還需要其他幫助嗎?
''', emojis=emoji)
    # message = TextMessage(text=event.message.text)
    # line_bot_api.reply_message(event.reply_token, message)
    
    sticker_message = StickerMessage(
        package_id='11538',
        sticker_id='51626494'
    )
    
    buttons_template = TemplateSendMessage(
            alt_text= '小幫手 template',
            template=ButtonsTemplate(
                title='選擇服務',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/ZgZ5lME.jpg',
                actions=[
                    MessageTemplateAction(
                        label='查詢油價',
                        text='查詢油價'
                    ),
                    MessageTemplateAction(
                        label='查詢匯率',
                        text='查詢匯率'
                    ),
                    MessageTemplateAction(
                        label='查詢股價',
                        text='查詢股價'
                    )
                ]
            )
        )
    line_bot_api.reply_message(
        event.reply_token, 
        [text_message,sticker_message,buttons_template]
    )
    
def push_msg(event,msg):
    try:
        user_id = event.source.user_id
        line_bot_api.push_message(user_id, TextSendMessage(text=msg))
    except:
        room_id = event.source.user_id
        line_bot_api.push_message(room_id, TextSendMessage(text=msg))
    
def Usage(event):
    push_msg(event, " 👀 查詢方法 👀 \
                    \n\
                    \n 小幫手可查詢油價➡️匯率➡️股價\
                    \n\
                    \n 油價通知 ➡️➡️➡️ 輸入查詢油價\
                    \n 股價通知 ➡️➡️➡️ 輸入查詢'股票代號'\
                    \n 匯率通知 ➡️➡️➡️ 輸入查詢匯率\
                    \n 匯率兌換 ➡️➡️➡️ 輸入換匯USD/TWD")
