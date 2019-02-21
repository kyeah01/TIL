# Django_intro 실습

* 강의에서 활용하였던 `utilities` app 을 이용해 다양한 유틸 앱으로 만들어보자.


### url 정보

|          url          |                                                          |
| :-------------------: | :------------------------------------------------------: |
|      utilities/       |                                                          |
|    utilities/bye/     |             우리 헤어지는 시간 출력하기2.28              |
| utilities/graduation/ |      우리 1학기 졸업시간까지 남은 날짜 출력하기5.28      |
| utilities/imagepick/  |        Lorem Picsum 활용하여 랜덤 이미지 출력하기        |
|   utilities/today/    | 오늘 시간 및 날씨 정보 알려주기(지금 살고 있는 기준으로) |
| utilities/ascii_new/  |       ascii art를 변환을 위한 text, font 입력받기        |
| utilities/ascii_make/ |        artii를 활용하여 art로 만들어서 출력해주기        |
|  utilities/original/  |             영어 번역을 위한 한국어 입력받기             |
| utilities/translated/ |            papago 활용하여 한-영 번역 해주기             |

---

### 활용 정보

* `utilities/imagepick/`

  * 구글 검색 'lorem picsum'

  * 다음의 url 설정을 통해 이미지를 만들어주기.

    ```python
    https://picsum.photos/500/500/?random
    ```

* `utilites/today/`

  * 오늘 날씨 알아보기

    * API 정보

      ```python
      https://openweathermap.org/current
      ```

    * 요청 url

      ```python
      https://api.openweathermap.org/data/2.5/weather?q=Seoul,kr&lang=kr&APPID="+key
      ```


* `utilities/ascii_make/`

  * 입력받은 정보를 통해서 [artii](http://artii.herokuapp.com) 에서 정보 가져오기

    ```
    http://artii.herokuapp.com/make?text=ASCII&font=short
    ```

  * 사용자로부터 입력 받을 때, font는 아래 중에서 선택할 수 있게 하기 *나중에 반복문 보여줌*

    ```python
    fonts = ['short', 'utopia', 'rounded', 'acrobatic', 'alligator']
    ```

* `utilities/translated/`

  * 네이버 파파고(SMT 번역) 활용하기

    ```python
    naver_client_id = os.getenv("NAVER_CLIENT_ID")
    naver_client_secret = os.getenv("NAVER_CLIENT_SECRET")
    
    papago_url = "https://openapi.naver.com/v1/papago/n2mt"
    # 네이버에 Post 요청을 위해서 필요한 내용들
    headers = {
        "X-Naver-Client-Id": naver_client_id,
        "X-Naver-Client-Secret": naver_client_secret
    }
    data = {
        "source": "ko",
        "target": "en",
        "text": text[4:]
    }
    papago_response = requests.post(papago_url, headers=headers, data=data).json()
    print(papago_response)
    reply_text = papago_response["message"]["result"]["translatedText"]
    ```
