# FLASK

## 시작하기 전에

- web을 구동하기 위해서는 원래 WSGI(Web Server Gateway Interface) 규격에 맞게 어플리케이션을 생성해 실행해야 하는데, flask에서는 WSGI를 위한 Microframe를 지원한다.

- flask는 Python의 class datatype이며

- create instance of web application(s)를 위한 framework다.

- pip를 통해 install할 수 있다.

  > pip install flask

- FLASK로 만들어보는 WSGI 어플리케이션.

  flask와  WSGI에 대한 설명이 자세해서 읽어보면 좋을 듯.

  https://spoqa.github.io/2012/01/16/wsgi-and-flask.html





## Flask 초기세팅하기

- python 3.6.7버전과 가상환경 구축을 위한 pyenv-virtualenv를 설치하는 경우를 예로 한다. ( ubuntu openssl 이슈가 존재한다고 한다. )

- 차례대로 진행하면 된다.

- pyenv : 파이썬 버전을 관리하는 툴, 하나의 컴퓨터에 다양한 파이썬 버전을 설치하고 관리한다.

  ~~~bash
  # pyenv 설치
  $ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
  ~~~

  ~~~bash
  # python 설치
  $ pyenv install 3.6.7
  $ pyenv global 3.6.7
  $ pyenv rehash
  $ python -V					# 설치된 python의 버전 확인
  $ pyenv versions			# 설치된 pyenv의 버전 확인
  ~~~

- pyenv-virtualenv : 파이썬 환경을 격리하는 툴로 pyenv의 확장 플러그인이다. 파이썬 버전과 라이브러리의 완전한 격리 환경을 제공한다.

  ~~~bash
  # pyenv-virtualenv 설치
  $ git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
  ~~~

  ~~~bash
  # 가상환경 만들기
  $ pyenv virtualenv <파이썬버전> <가상환경 이름>
  							# (1) 특정 파이썬 버전으로 가상환경 생성하는 경우
  $ pyenv virtualenv <가상환경이름>
  							# (2) 그냥 현재 파이썬 버전으로 생성하는 경우
  
  $ pyenv versions			# pyenv 를 이용해 만든 파이썬 버전들을 출력
  $ pyenv virtualenvs			# 설치된 가상환경 목록만 확인
  ~~~

  ~~~bash
  # global로 가상환경 활성화하기
  $ pyenv activate <가상환경 이름>
  # 활성화되면 커맨드라인 앞에 가상환경 이름이 나옴.
  # 예시) (test37) yourid:~/workspace/ $
  
  # 가상환경 비활성화
  $ pyenv deactivate
  ~~~

  ~~~bash
  # local로 가상환경 활성화하기 : 로컬로 활성화하면 해당 디렉토리 빠져나올 시 자동으로 비활성화된다.
  # 반드시 가상환경으로 지정할 디렉토리로 이동한 후에 활성화시켜야 한다.
  # 현재 디렉토리를 특정 가상환경으로 설정한다는 의미이기 때문이다.
  $ pyenv local <가상환경 이름>
  ~~~

  ~~~bash
  # 가상환경을 완전히 삭제하고 싶다면
  # 이 경우 다시 사용을 위해서는 install이 다시 필요하다
  # 단순히 local과 global을 혼동했다던가 하는 이유로는 deactive만 활용해도 충분하다.
  $ pyenv uninstall <가상환경 이름>
  ~~~


- pip : 파이썬 라이브러리를 관리한다.

  ~~~bash
  $ pip install -U pip			# 설치와 업그레이드
  $ pip list						# 설치된 파이썬 패키지 목록조회
  ~~~







## FLASK WORK!

- 플라스크 설치

  ~~~bash
  $ pip install flask
  ~~~

- 이제 플라스크를 import하여 사용할 수 있게 되었다.

- 파일명은 자유로 설정할 수 있지만, flask.py는 사용해서는 안되며, app.py를 사용하는 것이 기본적인 원칙이다. app.py가 아닐 경우 다른 방식의 실행방법이 필요하다

  ~~~bash
  # app.py가 아닐 경우 (project.py라고 하자)
  $ export FLASK_APP=project.py  #를 선언해 준 이후에야 run 시킬 수 있다.
  ~~~

- 서버를 구동시켜보자.

  ~~~bash
  $ flask run --host=0.0.0.0 --port=8080
  # $ flask run --host 0.0.0.0 --port 8080 로도 가능.
  $ flask run --host=$HOST --port=$PORT
  # $ flask run -h $IP -p $PORT 마찬가지.
  ~~~

- 서버를 끄지 않고 계속 구동하기 위한 코딩.

  ~~~python
  from flask import Flask
  
  # 플라스크 초기화
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

~~~python
@app.route('/')
def method():
    return 'a'
~~~

- Route


  ~~~python
  @app.route('/users/create')
  # unique한 페이지 url
  @app.route('/users/create/')
  # 얘는 후방 슬래시 있어도 잡고 없어도 잡음.
  # 더 정확히는 후방 슬래시 없이 액세스 하면 슬래시가 있는 url로 잡아줌
  ~~~





## GET, POST

- Get방식과 Post방식의 차이
  (https://interconnection.tistory.com/72 참조.)

  - Get
    ![](C:\Users\강예원\Desktop\TIL\MD_Image\WEB\flask\GET.png)
    - 가져온다는 개념에 가깝다. 서버의 어떤 값이나 내용, 상태를 바꾸지 않고 보여줄때 사용한다(검색이나 게시판 조회 같은 경우)
    - 입력받은 query의 이름과 값이 결합되어 스트링 형태로 서버에 전달된다. (URL에 query의 값이 그대로 노출된다.)
    - DB에 추가로 정보를 저장하거나 처리하지 않고 저장된 Data를 단순 요청하는 정도로 사용한다. 
    - 데이터 양의 제한 존재한다.
    
  - Post
    ![](C:\Users\강예원\Desktop\TIL\MD_Image\WEB\flask\POST.png)
    - 수행한다는 개념에 가깝다. 서버의 값이나 상태를 변경하는 경우에 사용한다(게시판에 글을 쓰거나 수정하는 경우)
    - 클라이언트와 서버간에 인코딩하여 서버로 전송됨.
    - 헤더를 통해 요청이 전송된다.
    - 데이터의 양은 제한이 없다.
    - DB에 추자로 서버에서 갱신작업을 할 때 서버에서 정보가 가공되어 응답하는 경우에 주로 사용한다.
  - GET과 POST 둘 다 보안에는 취약하고, 보안을 위해서는 2차 조치가 필요하다.

  

- c9에서 flask기반으로 데이터 주고받기

  - html을 python에서 열기 위해서 flask에서 지원하는 render_templates을 활용할 예정이다.

    ~~~python
    # 정보를 전송할 페이지 설계
    @app.route('/ping')
    def ping_new():
        return render_template('ping_new.html')
    ~~~

    ~~~html
    <!--렌더링 하는 html 파일의 form action설정-->
    <form action='/pong_new' method="POST">
        <input type="text" name="res"/>
        <input type="submit" value="Submit"/>
    </form>
    <!--action과 method 둘 다를 선언해 주어야 함.-->
    ~~~

    ~~~python
    # 정보를 수신할 페이지 설계, 마찬가지로 method 선언을 해주지 않으면 수신할 수 없다.
    @app.route('/pong_new', methods=['POST'])
    def pong_new():
        res = request.form.get('res')
        return render_template('pong_new.html', res=res)
    ~~~

    

  - request 모듈과 관련되어 정리된 페이지를 발견했다. 한번 읽어봐도 좋을 듯.
    https://dgkim5360.tistory.com/entry/python-requests





## URL Redirection

- URL forwarding이라고도 한다.
- 이용가능한 웹페이지를 하나이상의 url주소로 만들어주는 웹기법.
- 플라스크에서는 url_for와 redirect를 조합해서 url redirection이 가능하다.
- url_for로 url을 생성하고, redirect로 이동한다고 생각하면 된다!
- url_for는 주소를 받지 않고 뷰함수 이름을 받는다.

~~~python
url_for('index')
return redirect(url_for('index'))
~~~






## JINJA를 통한 TEMPLATE 상속

- jinja를 사용해 template도 상속해서 쓸 수 있다.

- base가 되는 template 생성. 별다른 특이점 없이 생성한다.

- 자식 템플릿에서 extend 명령어를 통해 상속받는다.

  ~~~python
  {% extends "base.html" %}
  ~~~


- base template에서 원하는 부분을 수정하기 위해 block을 선언할 수 있음. 파생 template이 변경할 수 있는 부분(항목)을 정의함.

  ~~~html
  {% block head %} {% endblock %}
  {% block head %} {% endblock head %}
  <!-- 와 같이도 쓸 수 있으나, 권장하지 않는다. 완전히 알아보기 어려울때만 사용할 것.-->
  ~~~

- 부모템플릿에서 선언한 것과 똑같이 선언해서 자식템플릿에서 호출한다. block선언부가 대체된다고 생각하면 된다.

  ~~~html
  {% block head %} {% endblock %}
  ~~~

- 대체되는게 아니라 부모의 블락내 내용을 그대로 받아오고, 그 뒤에 add하고싶다면 block선언부 내에 super를 선언해서 해결할 수 있다.

  ~~~html
  {{ super() }}
  ~~~




## Modular Applidation with Blueprints

~~~html
<link rel="icon" href="{{url_for('static', filename='favicon.png')}}" type="image/png"/>
~~~

- 왜 템플릿은 템플릿 폴더에 넣어야 하고 이미지는 스태틱폴더에 넣어야 하는지에 대한 이야기
  http://flask.pocoo.org/docs/1.0/blueprints/?highlight=static
- 한마디로 축약하자면 모듈화의 편리성을 위해 flask에서 미리 설정해둔 규칙이라는 것.







##### Reference

https://github.com/djpy2/TIL/blob/master/doc/c9_python_setting.md

https://www.python.org/dev/peps/pep-0333/#the-application-framework-side

https://pythonhow.com/how-a-flask-app-works/

https://spoqa.github.io/2012/01/16/wsgi-and-flask.html

http://flask.pocoo.org/docs/1.0/

http://taewan.kim/post/python_virtual_env/

https://interconnection.tistory.com/72

위키백과 - URL 리다이렉션

