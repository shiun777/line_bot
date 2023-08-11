from line_bot_api import *
import requests
import twder

def getCurrencyName(currency):
    currency_list = { 
        "USD" : "美元",
        "JPY": "日圓",
        "HKD" :"港幣",
        "GBP": "英鎊",
        "AUD": "澳幣",
        "CAD" : "加拿大幣",
        "CHF" : "瑞士法郎",  
        "SGD" : "新加坡幣",
        "ZAR" : "南非幣",
        "SEK" : "瑞典幣",
        "NZD" : "紐元", 
        "THB" : "泰幣", 
        "PHP" : "菲國比索", 
        "IDR" : "印尼幣", 
        "KRW" : "韓元",   
        "MYR" : "馬來幣", 
        "VND" : "越南盾", 
        "CNY" : "人民幣",
      }
    try: currency_name = currency_list[currency]
    except: return "無可支援的外幣"
    return currency_name

def getExchangeRate(msg):
    """
    sample
    code = '換匯USD/TWD/100'
    code = '換匯USD/JPY/100'
    """
    currency_list = msg[2:].split("/")
    currency = currency_list[0]
    currency1 = currency_list[1]
    money_value = currency_list[2]
    url_coinbase = 'https://api.coinbase.com/v2/exchange-rates?currency=' + currency
    res = requests.get(url_coinbase)
    jData = res.json()
    pd_currency = jData['data']['rates']
    content = f'目前的兌換率為:{pd_currency[currency1]} {currency1} \n查詢的金額為:'
    amount = float(pd_currency[currency1])
    content += str('%.2f' % (amount * float(money_value))) + " " + currency1
    return content
  
def showCurrency(code) -> "JPY":
    content = ""
    currency_name = getCurrencyName(code)
    if currency_name == "無可支援的外幣": return "無可支援的外幣"
    currency = twder.now(code)
    now_time = str(currency[0])
    buying_cash = "無資料" if currency[1] == '-' else str(float(currency[1]))
    sold_cash = "無資料" if currency[2] == '-' else str(float(currency[2]))
    buying_spot = "無資料" if currency[3] == '-' else str(float(currency[3]))
    sold_spot = "無資料" if currency[4] == '-' else str(float(currency[4]))
    content +=  f"{currency_name} 最新掛牌時間為: {now_time}\n ---------- \n 現金買入價格: {buying_cash}\n 現金賣出價格: {sold_cash}\n 即期買入價格: {buying_spot}\n 即期賣出價格: {sold_spot}\n \n"
    return content