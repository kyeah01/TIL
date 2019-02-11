
import requests
from bs4 import BeautifulSoup

req = requests.get("https://m.stock.naver.com/marketindex/index.nhn").text
soup = BeautifulSoup(req, 'html.parser')
test = soup.select(".stock_dn")

# marketindexLastList > li.stock_dn.zar > a > div.item_wrp > span.stock_item
# marketindexLastList > li.stock_dn.zar > a > div.price_wrp > span
# marketindexLastList > li.stock_dn.zar > a > div.item_wrp
#marketindexLastList > li.stock_dn.zar
#marketindexLastList > li.stock_dn.zar

for i in test:
    day = soup.select_one(".stock_item")
    price = soup.select_one(".price_wrp > span")
    print(day,price)