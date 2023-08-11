# from pymongo import MongoClient
# import datetime

# stockDB ='mydb'
# dbname = 'test-good1'

# def constructor_stock():
#     client = MongoClient("mongodb://o3335577:3335577@ac-nzt7vkj-shard-00-00.mc9jndu.mongodb.net:27017,ac-nzt7vkj-shard-00-01.mc9jndu.mongodb.net:27017,ac-nzt7vkj-shard-00-02.mc9jndu.mongodb.net:27017/?ssl=true&replicaSet=atlas-cb4ks6-shard-0&authSource=admin&retryWrites=true&w=majority")
#     db = client[stockDB]
#     return db


# ####### 更新股票的名稱
# def update_my_stock(user_name, stockNumber, condition, target_price):
#     db = constructor_stock()
#     collect = db[user_name]
#     collect.update_many({"favorite_stock": stockNumber }, {'$set': {'condition': condition, "price": target_price}})
#     content = f"股票{stockNumber}更新成功"
#     return content
    
# ####### 新增使用者的股票

# def write_my_stock(userID, user_name, stockNumber, condition, target_price):
#     db = constructor_stock()
#     collect = db[user_name]
#     is_exit = collect.find_one({"favorite_stock": stockNumber})
#     if is_exit != None :
#         content = update_my_stock(userID, user_name, stockNumber, condition, target_price)
#         return content
#     else:
#         collect.insert_one({
#             "userID": userID,
#             "favorite_stock": stockNumber,
#             "cindition": condition,
#             "price": target_price,
#             "tag": "stock",
#             "date_info": datetime.now()
#         })
#     return f"{stockNumber}以新增至你的股票清單"
    
    
    
from pymongo import MongoClient
import datetime
from bs4 import BeautifulSoup
import requests
# Authentication Database認證資料庫
stockDB='mydb'
dbname = 'howard-good31'

def constructor_stock(): 
    client = MongoClient("mongodb://o3335577:3335577@ac-nzt7vkj-shard-00-00.mc9jndu.mongodb.net:27017,ac-nzt7vkj-shard-00-01.mc9jndu.mongodb.net:27017,ac-nzt7vkj-shard-00-02.mc9jndu.mongodb.net:27017/?ssl=true&replicaSet=atlas-cb4ks6-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client[stockDB]
    return db

#----------------------------更新暫存的股票名稱--------------------------
def update_my_stock(user_name,  stockNumber, condition , target_price):
    db=constructor_stock()
    collect = db[user_name]
    collect.update_many({"favorite_stock": stockNumber }, {'$set': {'condition':condition , "price": target_price}})
    content = f"股票{stockNumber}更新成功"
    return content
#   -----------    新增使用者的股票       -------------
def write_my_stock(userID, user_name, stockNumber, condition , target_price):
    db=constructor_stock()
    collect = db[user_name]
    is_exit = collect.find_one({"favorite_stock": stockNumber})
    if is_exit != None :
        content = update_my_stock(user_name, stockNumber, condition , target_price)
        return content
    else:
        collect.insert_one({
                "userID": userID,
                "favorite_stock": stockNumber,
                "condition" :  condition,
                "price" : target_price,
                "tag": "stock",
                "date_info": datetime.datetime.now()
            })
    return f"{stockNumber}已新增至您的股票清單"

#------------------秀出使用者的股票條件------------------
def show_stock_setting(user_name, userID) :
    db = constructor_stock()
    collect = db[user_name]
    dataList = list(collect.find({"userID": userID}))
    if dataList == []: return "你的股票清單為空，請新增股票至清單中"
    content = "你清單中的選股條件為: \n"
    for i in range (len(dataList)):
        content += f'{dataList[i]["favorite_stock"]}{dataList[i]["condition"]}{dataList[i]["price"]}\n'
    
    # for data in dataList:
    #     stock_setting = f"{data['favorite_stock']} {data['condition']}{dataList[i]["price"]}\n"
    #     content += stock_setting
    
    return content

#------------------ 刪除股票 --------------------------
def delete_my_stock(user_name, stockNumber):
    db = constructor_stock()
    collect = db[user_name]
    collect.delete_one({'favorite_stock': stockNumber})
    return stockNumber + "刪除成功"

#------------------ 刪除所有股票 -----------------------
def delete_my_allstock(user_name, userID):
    db = constructor_stock()
    collect = db[user_name]
    collect.delete_many({'userID': userID})
    return "全部刪除成功"