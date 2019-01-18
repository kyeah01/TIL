import requests

# req = requests.get("https://google.com")
# print(req)
# print(req.text)
# print(req.status_code)

from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')
kospi = soup.select_one('#KOSPI_now')

print(kospi.text)




# soup = BeautifulSoup.(req, 'html.parser')
# kospi = soup.select_one('경로')