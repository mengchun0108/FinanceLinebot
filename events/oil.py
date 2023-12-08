import requests
from bs4 import BeautifulSoup
# 油價查詢
def oil_price():
    target_url = 'http://gas.goodlife.tw/'
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    title = soup.select('#main')[0].text.replace('\n', '').split('(')[0]
    #gas_price = soup.select('#gas-price')[0].text.replace(' ','')[0]
    #gas_price = soup.select('#gas-price')[0].text.replace('\n\n\n', '').replace(' ','')[0]
    cpc = soup.select('#cpc')[0].text.replace('95油價', '95')
    cpc = cpc.replace("油價","油價⛽")
    content = '{}{}'.format(cpc, title)
    return content