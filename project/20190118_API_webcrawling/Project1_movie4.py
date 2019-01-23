import csv, requests

with open('movie_naver.csv', 'r', newline='', encoding='UTF-8') as f:
    movies = csv.DictReader(f)
    for movie in movies:
        image_url = movie['image']
        movie_code = movie['movie code']
        res = requests.get(image_url)
        with open(f"images/{movie_code}.jpg", 'wb') as f:
            f.write(res.content)