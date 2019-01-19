import requests, os, json, csv, datetime

finalDt = datetime.datetime(2019, 1, 13)
ago = datetime.timedelta(days=-7)
moviecodelist = []
token = os.getenv("API_key")

# 문제 1번
with open('boxoffice.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ('movieCd', 'movieNm', 'audiAcc', 'date')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for weeks in range(10):
        targetDt = (finalDt + ago*weeks).strftime('%Y%m%d')                             # 날짜를 7일씩 바꿔주게 설정
        url_box = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={token}&targetDt={targetDt}&weekGb=0'
        rank = requests.get(url_box).json() 
        data = rank['boxOfficeResult']['weeklyBoxOfficeList']
        for i in range(10):
            if data[i]['movieCd'] not in moviecodelist:
                moviecodelist.append(data[i]['movieCd'])
                writer.writerow({fieldname:data[i][fieldname] if fieldname != 'date' else targetDt
                                 for fieldname in fieldnames})