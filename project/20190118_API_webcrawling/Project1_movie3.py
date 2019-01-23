import requests, csv, json, os

n_id = os.getenv("N_API_ID")
n_pw = os.getenv("N_API_PW")
headers = {"X-Naver-Client-Id" : n_id,
                "X-Naver-Client-Secret" : n_pw}

with open('movie_naver.csv', 'w', newline='', encoding='UTF-8') as f:
    fieldnames = ('movie code', 'image', 'link', 'userRating')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    with open('movie.csv', 'r', newline='', encoding='UTF-8') as moviefile:
        movies = csv.DictReader(moviefile)
        for movie in movies:
            movieNm = movie['movieNm']
            movieCd = movie['movieCd']
            url = f'https://openapi.naver.com/v1/search/movie.json?query={movieNm}'
            req = requests.get(url, headers = headers).json()
            movie_list = req['items'][0]
            writer.writerow({fieldname : movie_list[fieldname] if fieldname != 'movie code' else movieCd
                                      for fieldname in fieldnames})