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

# def getExchangeRate(msg):
# # 不同貨幣直接換算（非只限於台幣）
#     """
#     sample
#     code = '換匯USD/TWD/100;
#     code = '換匯USD/JPY/100'
#     """
#     currency_list = msg[2:].split("/")
#     currency = currency_list[0]
#     currency1 = currency_list[1]
#     money_value = float(currency_list[2])
#     url_coinbase = 'https://api.coinbase.com/v2/exchange-rates?currency=' + currency
#     res = requests.get(url_coinbase)
#     jData = res.json()
#     pd_currency = jData['data']['rates']
#     amount = float(pd_currency[currency1])
#     content = "目前的兌換率為：" + str(amount) + " " + currency1 + "\n查詢的金額為："
#     content += str(round(amount * (money_value), 4)) + " " + currency1
#     return content

def get_exchange_rate(currency):
    session = requests.Session()
    url_coinbase = f'https://api.coinbase.com/v2/exchange-rates?currency={currency}'
    res = session.get(url_coinbase)
    jData = res.json()
    return jData['data']['rates']

def main(msg):
    currency_list = msg[2:].split("/")
    currency = currency_list[0]
    currency1 = currency_list[1]
    money_value = float(currency_list[2])

    pd_currency = get_exchange_rate(currency)
    amount = float(pd_currency[currency1])

    content = f"目前的兌換率為：{amount} {currency1}\n查詢的金額為：{round(amount * money_value, 4)} {currency1}"

    return content


# 查詢匯率
def showCurrency(code) -> "JPY": 
# code 為外幣代碼
    content = ""
    currency_name = getCurrencyName(code)
    if currency_name == "無可支援的外幣": return "無可支援的外幣"
    # 資料格式{貨幣代碼：(時間, 現金買入, 現金賣出, 即期買入, 即期賣出), ...}
    currency = twder.now(code)
    # 當下時間
    now_time = str(currency[0])
    # 銀行現金買入價格
    buying_cash = "無資料" if currency[1] == '-' else str(float(currency[1]))
    # 銀行現金賣出價格
    sold_cash = "無資料" if currency[2] == '-' else str(float(currency[2]))
    # 銀行即期買入價格
    buying_spot = "無資料" if currency[3] == '-' else str(float(currency[3]))
    # 銀行即期賣出價格
    sold_spot = "無資料" if currency[4] == '-' else str(float(currency[4]))
    content +=  f"{currency_name} \n -------------------- \n 現金買入價格: {buying_cash}\n 現金賣出價格: {sold_cash}\n 即期買入價格: {buying_spot}\n 即期賣出價格: {sold_spot} \n\n最新掛牌時間為: {now_time}"
    return content