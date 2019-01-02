
import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.naver.com/").text
soup = BeautifulSoup(req, 'html.parser')
test = soup.select(".PM_CL_realtimeKeyword_rolling_base .ah_item")

# test_numb = soup.select(".PM_CL_realtimeKeyword_rolling_base .ah_item .ah_r ")
# test_name = soup.select(".PM_CL_realtimeKeyword_rolling_base .ah_item .ah_k ")

for i in test:

    test_numb = soup.select_one(".ah_r ")
    test_name = soup.select_one(".ah_k ")
    
    print(i.text)