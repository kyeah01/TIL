import os, requests, json, datetime, csv

key = os.getenv('API_key')                                                    # 키값을 import 하여 사용
Date = datetime.date(2019,1,13).strftime('%Y%m%d')      # search target date time 수정 필요(연속적인 값으로)
                                                                                          #  총 10주이며, 기준일(마지막 일자)은 2019년 1월 13일
url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={Date}&weekGb=0'
req = requests.get(url).json()                              # request.get을 통해 얻은 결과값을 jason으로 바로 가공
BoxOfficeList = req['boxOfficeResult']['weeklyBoxOfficeList']
print(BoxOfficeList)
                                    #결과값이 'boxOfficeResult'라는 하나의 큰 딕셔너리로 묶여있어 내부 데이터로 들어가기 위해 키값 호출
                                    # 호출된 결과값 중 뽑아내야 하는 데이터값이 다시 'weeklyBoxOfficeList'에 밸류값으로 들어있어 한번 더 키값 호출
# 영화 대표코드 , 영화명 , 해당일 누적관객수 , 해당일을 뽑아내야 함
# 'movieCd', 'movieNm', 'audiAcc'가 뽑아올 수 있는 각 명칭, 해당일은 req['boxOfficeResult']에서 ['showRange']로 뽑아낼 예정

with open ('movie2.csv', 'w') as moviefile:
    names = ('movieCd', 'movieNm', 'audiAcc', 'Date')
    writer = csv.DictWriter(moviefile,fieldnames=names)
    writer.writeheader()
    for idx in range(10):
        writer.writerow({name:BoxOfficeList[name]  if name != 'Date' else req[idx]['boxOfficeResult']['showRange']
                                                   for name in names})