import requests

req = requests.get("https://www.naver.com/")

# print(req)
print(req.text)
# print(req.status_code)