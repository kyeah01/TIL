import requests, os, json, csv, datetime
from pprint import pprint
from bs4 import BeautifulSoup

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


# 문제 2번
with open('movie.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ('movieCd', 'movieNm','movieNmEn', 'movieNmOg', 'openDt', 'showTm', 'genres', 'directors', 'audits', 'actors1', 'actors2', 'actors3')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for code in moviecodelist:
        url_mov = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={token}&movieCd={code}'
        movie_information = requests.get(url_mov).json()
        movie_inform = movie_information["movieInfoResult"]["movieInfo"]
        imsi = {}
        for fieldname in fieldnames:
            if fieldname == 'genres':
                imsi.update({fieldname : movie_inform[fieldname][0]['genreNm']})
            elif fieldname == 'directors':
                imsi.update({fieldname : movie_inform[fieldname][0]['peopleNm']})
            elif fieldname == 'audits':
                imsi.update({fieldname : movie_inform[fieldname][0]['watchGradeNm']})
            elif fieldname == 'actors1':
                if len(movie_inform['actors']) >= 1:
                    imsi.update({fieldname : movie_inform['actors'][0]['peopleNm']})
                else:
                    imsi.update({fieldname :''})
            elif fieldname == 'actors2':
                if len(movie_inform['actors']) >= 2:
                    imsi.update({fieldname : movie_inform['actors'][0]['peopleNm']})
                else:
                    imsi.update({fieldname :''})
            elif fieldname == 'actors3':
                if len(movie_inform['actors']) >= 3:
                    imsi.update({fieldname : movie_inform['actors'][0]['peopleNm']})
                else:
                    imsi.update({fieldname :''})
            else:
                imsi.update({fieldname : movie_inform[fieldname]})
        writer.writerow({lists:imsi[lists] for lists in imsi})                  # 마지막으로 프린트

3. 문제 3번