from line_bot_api import *
from events.basic import *
from events.oil import *
from events.Msg_Template import *
from events.EXRate import *
from events.map import *
from model.mongodb import*
import re
import twstock
import datetime
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)

#---------------------------抓使用者關心的股票
def cache_users_stock():
    db = constructor_stock()
    nameList = db.list_collection_names()
    users = []
    for i in range(len(nameList)):
        collect = db[nameList[i]]
        cel = list(collect.find({"tag":'stock'}))
        users.append(cel)
    return users

#---------------------------監聽
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

#----------------------------處理
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    profile = line_bot_api.get_profile(event.source.user_id)
    uid = profile.user_id
    messages_text = str(event.message.text).lower()
    msg = str(event.message.text).upper().strip()
    emsg = event.message.text
    user_name = profile.display_name
    stockNumber = ""
    
    ######## -----------------------------適用說明 選單 油價查詢-----------------------------
    if messages_text == '@使用說明':
        about_us_event(event)
        Usage(event)

    if messages_text == '附近資訊':
        google_map(event)  

    if event.message.text == '附近停車場':
        user_id = event.source.user_id
        api_key = "AIzaSyBuh_ZmBbKBjvtG95pGzaW2-bf77Vc2QoY"

        user_location = f"{event.message.latitude},{event.message.longitude}"
        radius = 1000
        api_key = "AIzaSyBuh_ZmBbKBjvtG95pGzaW2-bf77Vc2QoY"

        nearby_parking = search_nearby_parking(user_location, radius, api_key)
                
        if nearby_parking:
            reply_text = '附近的停車場有：\n'
            for parking in nearby_parking:
                name = parking['name']
                address = parking['vicinity']
                reply_text += f'名稱: {name}\n地址: {address}\n----------\n'
        else:
            reply_text = '附近沒有找到停車場。'

        line_bot_api.reply_message(
            event.reply_token,
            TextMessage(text=reply_text)
        )




    if event.message.text == "想知道油價":
        content = oil_price()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
    ########## -----------------------------股票------------------------------------
    if event.message.text == "查詢股價":
        line_bot_api.push_message(uid, TextSendMessage("請輸入#加股票代號"))
        
    if re.match("想知道股價", msg):
        stockNumber = msg[5:]
        btn_msg = stock_reply_other(stockNumber)    
        line_bot_api.push_message(uid, btn_msg)
        return 0
    #新增使用者關注股票到mongodb
    # if re.match('關注[0-9]{4}[<>][0-9]',msg):
    #     stockNumber = msg[2:]
    #     line_bot_api.push_message(uid, TextSendMessage("加入股票代號"+stockNumber))
    #     content = write_my_stock(uid, user_name, stockNumber, msg[6:8], msg[7:])
    #     line_bot_api.push_message(uid, TextSendMessage(content))
    #     return 0
    
    if re.match('^關注[0-9]{4}[<>][0-9]{1,3}$', msg):
        stockNumber = msg[2:6]
        condition = msg[6]
        price = msg[7:]
        line_bot_api.push_message(uid, TextSendMessage("加入股票代號" + stockNumber))
        content = write_my_stock(uid, user_name, stockNumber, condition, price)
        line_bot_api.push_message(uid, TextSendMessage(content))
    
    if re.match('股票清單',msg):
        line_bot_api.push_message(uid, TextSendMessage("請稍等..."))
        content = show_stock_setting(user_name, uid)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
        
    if re.match('刪除[0-9]{4}',msg):
        line_bot_api.push_message(uid, TextSendMessage("請稍等..."))
        content = delete_my_stock(user_name, msg[2:])
        line_bot_api.push_message(uid, TextSendMessage(content))
        
    
    if re.match('清空股票',msg):
        line_bot_api.push_message(uid, TextSendMessage("請稍等..."))
        content = delete_my_allstock(user_name, uid)
        line_bot_api.push_message(uid, TextSendMessage(content))
        
    
    if(emsg.startswith('#')):
        text = emsg[1:]
        content = ''
        
        stock_rt = twstock.realtime.get(text)
        my_datetime = datetime.datetime.fromtimestamp(stock_rt['timestamp']+8*60*60)
        my_time = my_datetime.strftime('%H:%M:%S')
        
        content += '%s (%s) %s\n' %(
            stock_rt['info']['name'],
            stock_rt['info']['code'],
            my_time)
        content += '現價: %s / 開盤: %s\n'%(
            stock_rt['realtime']['latest_trade_price'],
            stock_rt['realtime']['open'])
        content += '最高: %s / 最低: %s\n'%(
            stock_rt['realtime']['high'],
            stock_rt['realtime']['low'])
        content += '量: %s\n' %(stock_rt['realtime']['accumulate_trade_volume'])
        
        stock = twstock.Stock(text)
        content += '-----\n'
        content += '最近五日價格: \n'
        price5 = stock.price[-5:][::-1]
        date5 = stock.date[-5:][::-1]
        for i in range(len(price5)):
            content += '[%s] %s\n' %(date5[i].strftime("%Y-%m-%d"), price5[i])
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content)
        )
        
    ###-----------------------------------匯率區---------------------------------------
    if re.match('幣別種類',emsg):
        message = show_Button()
        line_bot_api.reply_message(event.reply_token,message)
        
    if re.match("查詢匯率[A-Z]{3}",msg):
        line_bot_api.push_message(uid, TextSendMessage("請稍等..."))
        msg = msg[4:]
        content = showCurrency(msg)
        line_bot_api.push_message(uid,TextSendMessage(content))
        
    if re.match("換匯[A-Z]{3}/[A-Z{3}]",msg):
        line_bot_api.push_message(uid,TextSendMessage("將為你做外匯計算..."))
        content = getExchangeRate(msg)
        line_bot_api.push_message(uid,TextSendMessage(content))
        
    #-----------------------------------股價提醒-------------------------
    if re.match("股價提醒", msg):
        line_bot_api.push_message(uid, TextSendMessage("請稍等..."))
        import schedule
        import time
        #查看當前股價
        def look_stock_price(stock, condition, price, userID):
            print(userID)
            url = "https://tw.stock.yahoo.com/q/q?s=" + stock
            list_req = requests.get(url)
            soup = BeautifulSoup(list_req.content, "html.parser")
            getstock = soup.findAll("span")[11].text
            content = stock + "當前股市價格為:" + getstock
            if condition == '<':
                content += "\n篩選條件為: <" + price
                if float(getstock) < float(price):
                    content += "\n符合" + getstock + "<" + price + "的篩選條件"
                    line_bot_api.push_message(userID, TextSendMessage(text = content))
            elif condition == '>':
                content += "\n篩選條件為: >" + price
                if float(getstock) > float(price):
                    content += "\n符合" + getstock + ">" + price + "的篩選條件"
                    line_bot_api.push_message(userID, TextSendMessage(text = content))
            elif condition == '<':
                content += "\n篩選條件為: =" + price
                if float(getstock) == float(price):
                    content += "\n符合" + getstock + "=" + price + "的篩選條件"
                    line_bot_api.push_message(userID, TextSendMessage(text = content))
        def job():
            print('HH')
            line_bot_api.push_message(uid, TextSendMessage("問就是直接ALL IN"))
            dataList = cache_users_stock()
            for i in range(len(dataList)):
                for k in range(len(dataList[i])):
                    look_stock_price(dataList[i][k]['favorite_stock'], dataList[i][k]['condition'], dataList[i][k]['price'], dataList[i][k]['userID'])
        schedule.every(5).seconds.do(job).tag('daily-tasks-stock' + uid, "second")
    
        while True:
            schedule.run_pending()
            time.sleep(1)
    
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


