# FLASK

## 시작하기 전에

- web을 구동하기 위해서는 원래 WSGI(Web Server Gateway Interface) 규격에 맞게 어플리케이션을 생성해 실행해야 하는데, flask에서는 WSGI를 위한 Microframe를 지원한다.

- flask는 Python의 class datatype이며

- create instance of web application(s)를 위한 framework다.

- pip를 통해 install할 수 있다.

  > pip install flask

- FLASK로 만들어보는 WSGI 어플리케이션.

  falsk와  WSGI에 대한 설명이 자세해서 읽어보면 좋을 듯.

  https://spoqa.github.io/2012/01/16/wsgi-and-flask.html



## FLASK SERVER WORK!

- 서버를 끄지 않고 계속 구동하기 위한 코딩.

~~~python
from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)
    # __name__이 __main__이면 app의 run메소드를 실행시킴.
    # debug를 편의상 False로 놓을 수도 있음
    # 좀 더 정확하게 하기 위해 os모듈을 import하여 app.run의 파라미터로
    # host=os.getenv('IP'), port=os.getenv('PORT')
    # 와 같이 선언해 줄 수 있으나 하지않아도 무방.
~~~



## APP RUNNING!

- WSGI서버를 통해 

~~~python
@app.route('/')
def method():
    return 'a'
~~~



## GET, POST







flask에서 python기반으로 데이터 주고받기

1. html을 python에서 열기 위해서 flask에서 지원하는 render_templates를 활용할 예정이다.















##### Reference

https://pythonhow.com/how-a-flask-app-works/

https://spoqa.github.io/2012/01/16/wsgi-and-flask.html

