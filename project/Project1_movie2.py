import requests, os, json, csv


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