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





## model 설정하기

- 각 app에 있는 models.py 파일을 수정해서 반영한다. model설정.
- 

~~~python
class Board(models.Model):                      # 각 모델은 django.db.models.Model 클래스의 서브 클래스로 표현된다.
    title = models.CharField(max_length=10)     # 무한정 값을 가질 수 없으니까 필수인자로 무조건 max값을 가져야함.
                                                # 유효성 검사를 위해서도 필요.
    content = models.TextField()                # 얘는 제한이 없음
    created_at = models.DateTimeField(auto_now_add = True)
												# 장고모델이 최초저장시에만 현재 날짜를 적용
~~~

- 장고한테 이렇게 DB를 넣을꺼야 하고 말해줘야함

  ~~~bash
  $ python manage.py makemigrations boards
  ~~~

- 

- sqlite가 어떻게 되는지 확인하는 코딩

  ~~~bash
  $ python manage.py sqlmigrate boards 0001
  ~~~

  ~~~bash
  BEGIN;
  --
  -- Create model Board
  --
  CREATE TABLE "boards_board" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(10) NOT NULL, "content" text NOT NULL, "created_at" datetime NOT NULL);
  COMMIT;
  ~~~

- 값 주지 않아도 알아서 id값을 기본으로 pk로 가짐

- DB를 반영해주는거.


  ~~~bash
  $ python manage.py migrate
  ~~~

- python 인터프리터 장고에서 실행하기


  ~~~python
  python manage.py shell
  ~~~

- 장고 orm으로 

~~~python
>>> board = Board()
>>> board.title = 'first'
>>> board.content = 'django!'
>>> board.save()
>>> board.object.all()
~~~

-  import 꼬박꼬박 해주기 싫어!!
  장고에는 extension이라는게 있는데

  ~~~bash	
  $ pip install django-extensions
  ~~~

  로 설치하고 나서 settings의 installed_app에서

  ~~~python
  'django_extentions'
  ~~~

  그런다음에 

  ~~~bash
  $ python manage.py shell_plus
  ~~~

  로 들어오면 모두 import 되어있는것을 확인할 수 있다!!

  ~~~python
  >>> board = Board(title='second', content='django!!')
  >>> board.save()
  
  
  >>> Board.objects.create(title='third', content='django!!!')
  얘는 세이브가 필요없음
  ~~~



## CRUD

### Create

~~~python
>>> board = Board()
  >>> board.title = 'fourth'
  >>> board.content = 'django'
  >>> board.id
  >>> board.created_at
  >>> board.save()
  >>> board.id
  4
  >>> board.created_at
  datetime.datetime(2019, 2, 20, 10, 35, 33, 544975)
  >>> board = Board()
  >>> board.title = 'adfasdfasdfsadfasfasdfasdfasdfasdfasdf'
  >>> board.full_clean()
  # 장고가 얘를 검증해서 알려줌
~~~



### Read

~~~python
Board.objects.filter(title='first').all()
# title이 first인걸 전부 선택함
<QuerySet [<Board: 1: first>]>


Board.objects.filter(title='first').first()
<Board: 1: first>

하나만 뽑는거니까 위에랑 데이터 값이 다름

Board.objects.filter(title='missing').first()
# 없으면 none리턴

데이터가 어떻게 리턴되는지, 어디에 들어있는지 알아야 한다.
.get과 filter는 다르게 리턴되는 것을 알아야 한다.

포함되는거
boards = Board.objects.filter(title__contains='fi').all()

시작하는거
>>> boards = Board.objects.filter(title__startswith='fi').all()

오름차순
>>> boards = Board.objects.order_by('title').all()

내림차순
>>> boards = Board.objects.order_by('-title').all()


~~~



### Delete

~~~python
>>> board = Board.objects.get(pk=1)
>>> board.title = 'hello'
>>> board.save()
>>> board.title
'hello'
>>> board.delete()
(1, {'boards.Board': 1})
~~~



### Update









{{ board.created_at|timesince }}전







모듈 import하는 순서

같은 디렉토리에 있는 models를 가져온다고 쓴것. 명시적 상대 표현
1. 파이썬 표준 라이브러리를 제일 먼저 씀(os, random)
2. core django(django 프레임워크)에 내장되어 있는 것
3. third party library, pip install을 통해 사용하는 것들 (외부적으로 설치가 필요한것)
4. 장고 프로젝트 앱





## html Redirect

return render(request, 'boards/index.html')

html을 받아와서 보여주기때문에 표지페이지 같지만, index그 자체는 아니기때문에 진짜 index처럼 보이지는 않는다.

create는 model에 record를 생성하라는 요청을 보내기때문에, 단순히 페이지를 달라고 하는 요청의  get보다는  post가 의미상 더 적절하며, 모델과 관련된 데이터이기 때문에 url에 직접 보여지는 것은 좋지 않다. get이면 사용자가 url로 마음대로 주무를수 있다.

```python
return redirect('/boards/')
# redirect안에는 뷰함수, name이나 모델도 인자로 들어갈 수 있다.
```
