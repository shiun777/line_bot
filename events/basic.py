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
    line_bot_api.reply_message(
        event.reply_token,
        [text_message, sticker_message]
    )
