Django

1. template example
2. static example
   - 이미지 로딩하기
     load static
     "{% static '다운로드.png' %}" : 무조건 ""안에 DTL문법, 파일명은 확장명까지, ''안에.
   - css 로딩하기
   - css와 image는 따로 다시 폴더로 분할하여 사용한다.
3.  url분할하기
   - 앱이 여러개일때 똑같이 views이기때문에 확인할 수 없음.
   - 자기 앱만의 url을 생성하자.
   - url.py를 앱 내부에 다시 생성한다.
   - 

앱은 기능단위로 나눈다.

TEMPLATES extends를 위한 설정

원래 app dir먼저 봤지만

'DIRS': [os.path.join(BASE_DIR, 'django_intro', 't')],

'APP_DIRS': True,는 installed app에 설정된 dir에 있는 templates를 template으로 활용한다.