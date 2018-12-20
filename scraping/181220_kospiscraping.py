
import requests
from bs4 import BeautifulSoup

kospireq = requests.get("https://m.stock.naver.com/sise/siseIndex.nhn?code=KOSPI").text

print(kospireq)
dayall = []
priceall = []

soup = BeautifulSoup(kospireq,'html.parser')
al = soup.select(".div.ct_box.price")

#content > div > div.ct_box.price
#content > div > div.ct_box.price > table > tbody > tr:nth-child(1) > td:nth-child(1)
#content > div > div.ct_box.price > table > tbody > tr:nth-child(2) > td:nth-child(1)
#content > div > div.ct_box.price > table > tbody > tr:nth-child(1) > td:nth-child(2)

for i in al:
    dayall = soup.select(". tr:nth-child(1) > td:nth-child(1)")
    priceall = soup.select(". tr:nth-child(1) > td:nth-child(2)")

# for i in al:
print(dayall,priceall)