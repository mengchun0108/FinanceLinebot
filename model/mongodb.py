from pymongo import MongoClient
import datetime
from bs4 import BeautifulSoup
import requests
# Authentication Database認證資料庫
stockDB='testdb'
dbname = 'howard-good31'

def constructor_stock(): 
    client = MongoClient("mongodb://popcornbc0108:cuteflower0812@ac-cfbooje-shard-00-00.8to1mbr.mongodb.net:27017,ac-cfbooje-shard-00-01.8to1mbr.mongodb.net:27017,ac-cfbooje-shard-00-02.8to1mbr.mongodb.net:27017/?ssl=true&replicaSet=atlas-13bpwh-shard-0&authSource=admin&retryWrites=true&w=majority")
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
def write_my_stock(userID, user_name, stock_name, now_price , target_price):
    db=constructor_stock()
    collect = db[user_name]
    is_exit = collect.find_one({"favorite_stock": stock_name})
    if is_exit != None :
        content = update_my_stock(user_name, stock_name, now_price , target_price)
        return content
    else:
        collect.insert_one({
                "userID": userID,
                "favorite_stock": stock_name,
                "now_price" :  now_price,
                "price" : target_price,
                "tag": "stock",
                "date_info": datetime.datetime.now()
            })
        return f"{stock_name}已新增至您的股票清單"

#   -----------    秀出使用者的股票條件       -------------
def show_stock_setting(user_name, userID):
    db = constructor_stock()
    collect = db[user_name]
    dataList = list(collect.find({"userID": userID}))
    if dataList == []: return "您的股票清單是空的，請透過指令新增股票至清單中"
    content = "股票清單: "
    for i in range(len(dataList)):
        content = "\n" + dataList[i]["favorite_stock"] + "\n存入時價格: " + dataList[i]["now_price"] + "\n想關注價格: " + dataList[i]["price"]
    return content
#   -----------    刪除使用者特定的股票       -------------
def delete_my_stock(user_name, stockNumber):
    db = constructor_stock()
    collect = db[user_name]
    collect.delete_one({'favorite_stock': stockNumber})
    return stockNumber + "刪除成功"

#   -----------    刪除使用者股票清單內所有的股票       -------------
def delete_my_allstock(user_name, userID):
    db = constructor_stock()
    collect = db[user_name]
    collect.delete_many({'userID': userID})
    return "全部股票刪除成功"