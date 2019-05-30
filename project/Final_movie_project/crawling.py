from bs4 import BeautifulSoup
import requests

key = '8b39c67bad62bb2873c4ff640b9e414a'
target = '20190505'
url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={}&targetDt={}&weekGb=0'.format(key, target)

response = requests.get(url)
print(response.text)