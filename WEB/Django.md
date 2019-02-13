# Django

## 0. 준비사항

1. pyenv//python
   [Flask 초기세팅참고](https://github.comda/kyeah01/TIL/blob/master/WEB/Flask/FLASK.md)

- django는 풀스택 개발 툴이다.
- 프레임을 잘 해야 하는 웹프레임 언어가 있고, 해당 프로그래밍 언어를 잘 해야 하는 웹 프레임 언어가 있다.
- 장고는 파이썬을 잘 해야 웹 프레임 워크를 잘 다룰 수 있는 경우.
- 장고도 MVC: model view controll을 활용하지만 MTV:model template(다른 언어에서의 view) view라고 한다.
- .gitignore설정



## c9 초기 세팅하기

- 



## 프로젝트 만들기

- 먼저 project를 생성하자.
  ~~~bash
  # 장고 프로젝트 생성하기.
  # startproject까지는 고정, django_intro라는 이름을 가진 project를 지금 폴더에 생성한다는 뜻.
  # '-', django, class등 built-in method의 이름들은 사용할 수 없음.
  # django, test, class, django-test등은 프로젝트 이름으로 사용할 수 없습니다. 
  $ django-admin startproject django_intro .
  
  # 장고 서버 켜기
  $ python manage.py runserver $IP:$PORT
  ~~~

- initialize setting
  ~~~python
  # setting.py 파일을 수정해주자
  # Internationalization을 바꿔주자
  LANGUAGE_CODE = 'ko-kr'
  TIME_ZONE = 'Asia/Seoul'
  ~~~

- c9에서 Django를 구현하면 해 줘야 하는 설정(로컬은 필요없어요)

  ~~~python
  # c9 이라서 서버에러뜬다!
  # host를 허용해주자!
  # setting.py 파일을 수정해주자
  ALLOWED_HOSTS = ['dirname-id.c9users.io'] #를 사용하거나
  ALLOWED_HOSTS = ['*'] # 를 사용한다.
  ~~~


- 만들어진 프로젝트의 구조 확인하기

  ~~~bash
  $ tree
  
  ├── db.sqlite3
  ├── django_intro							# directory 내부에는 프로젝트를 위한 실제 파이썬 패키지들이 저장된다. 이 디렉토리 내의 이름을 이용하여 프로젝트 어디서나 파이썬 패키지들을 import할 수 있다.
  │   ├── __init__.py							# 파이썬으로 하여금 이 디렉토리를 패키지처럼 다루라고 알려주는 용도의 단순한 빈 파일.
  │   ├── __pycache__
  │   │   ├── __init__.cpython-36.pyc
  │   │   ├── settings.cpython-36.pyc
  │   │   ├── urls.cpython-36.pyc
  │   │   └── wsgi.cpython-36.pyc
  │   ├── settings.py							# 현재 장고 프로젝트의 모든 환경과 구성을 저장합니다.
  │   ├── urls.py								# 현재 장고 프로젝트의 url선언을 저장, 사이트의 url과 views의 연결을 지정.
  │   └── wsgi.py								# 현재 프로젝트를 서비스하기 위한 wsgi 호환 웹 서버의 진입점.
  └── manage.py								# 장고 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티
  ~~~

- 프로젝트 dir은 이름을 변경하면 안된다(내부 설정의 경로때문)
- '__init__'은 디렉토리를 패키지 형태로 다루기 위해 있는 생성자
- 세팅파일은 모든 환경설정을 구현한다. 주로 이곳에서 세팅수정 가능.
- 장고는 자체적으로 admin을 구현해준다. 관리자 페이지 구현하지 않아도 좋음. 초기 기본페이지에서 /admin/만 붙이면 된다.



## app 만들기

- 실제로 특정한 역할을 수행하는 것이 app이며 프로젝트는 이러한 어플리케이션의 집합이다.

- 하나의 프로젝트는 여러개의 어플리케이션을 가질 수 있다.

- 각각의 어플리케이션은 MTV 패턴으로 구성되어있다.

- 프로젝트 폴더 안에서 만든다. 프로젝트 manage project와 같은 높이에 dir을 가지지만 프로젝트 안에 들어있는 앱이라는 것을 생각하고 있어야 한다.

  ~~~bash
  # python manage.py startapp 'name'
  # 앱 마다마다 mtv를 가진다.
  $ python manage.py startapp home
  ~~~

  ~~~bash
  ├── __init__.py
  ├── admin.py			# 관리자용 페이지 수정(커스터마이즈)하는 곳
  ├── apps.py				# 앱의 정보가 있는 곳. 수정할 일이없음.
  ├── migrations			
  │   └── __init__.py		
  ├── models.py			# 앱에서 사용하는 모델을 정의하기 위한 공간.
  ├── tests.py			# test 코드를 작성하는 곳.
  └── views.py			# view들이 정의되는 곳, 사용자에게 어떻게 보여질지를 구현하는 곳.
  ~~~

- 이제 프로젝트에게 앱이 생겼음을 가르쳐주자
  프로젝트의 setting.py에 가서 수정한다.

  ~~~python
  INSTALLED_APPS = [
  'home.apps.HomeConfig',
  # appname의 apps.py의 세팅안에 있는 class명.
  # 마지막 쉼표를 작성해야 한다.
  # 'appname' 으로 써도 되지만, 그렇게 쓰면 나중에 환경설정이 힘듬
  ]
  ~~~





## app안의 MTV 구현하기.

- <sup>1</sup>  처리할 views를 만들고 <sup>2 </sup> 요청 url을 만들고 <sup>3</sup> 결과 보여줄 templates만들기.

- django에서 쓰는 {{}}는 jinja가 아니라 DTL [DTL 공식문서](https://docs.djangoproject.com/en/1.7/topics/templates/)

- 뷰 함수 만들기
  ~~~python
  # 장고는 뷰함수가 무조건 인자로 request를 받아야 함
  def index(request):
      return HttpResponse('Welcome to Django!')
  
  # 간단한 요청을 넘겨줄때 사용한다.
  return HttpResponse(인자)
  ~~~

- url 생성
  ~~~python
  # url.py
  # flask에서 app.route가 해줬던 일을 해줌
  # 무조건 뒤에 슬래시 붙여야 함.
  from home import views
  
  urlpatterns = [
      # 서버 주소, 작동할 함수, name은 필수가 아님
      path('home/index/', views.index, name='index'),
  ]
  ~~~

- templates를 활용한 return

  ~~~python
  # flask의 render_template와 같이 templates 폴더 안에 템플릿을 생성한다.
  # render 함수로 구현한다.
  # render함수는 request와 html 이름을 필수인자로 받고,
  # 인자를 넘겨주기 위해서는 반드시 딕셔너리를 활용해야 한다.
  # 딕셔너리가 아니라 QueryDict이긴 하지만 딕셔너리와 비슷하게 생각하면 된다.
  return render(request, 'dinner.html', {'menus' : menu, 'pick' : pick})
  ~~~



#### 

#### 저녁메뉴 리턴 실습

#### templates 실습

#### templates variable

- render()
  - render(request, template_name, context=None, context_type=None, status=None, using=None)



## 다른 페이지로 정보 넘기기

- GET 방식

  ~~~python
  def pong(request):
      print(request.GET)
      data = request.GET.get('data')
      return render(request, 'pong.html', {'data':data })
  ~~~

- POST 방식

  ~~~python
  def user_create(request):
      nickname = request.POST.get('nickname')
      password = request.POST.get('password')
      return render(request, 'user_create.html', {'nickname':nickname, 'password':password})
  ~~~

  ~~~html
  {% csrf_token %}
  ~~~

- csrf token을 사용해야 한다. middle ware 보안절차가 존재하기때문.

