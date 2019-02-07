# ORM : Object-Relational Mapping

- web application과 sql간의 소통을 위해서는 원래 SQL문으로 소통해야 한다.
  : 그러면 SQL을 잘 다뤄야 하고, 개발코드와 DB가 종속관계가 되어버린다.
- DB의 행, 테이블도 객체로 취급하면 어떨까? == **ORM**
- ORM은 일종의 번역기다. python코드를 sql로, sql코드를 python으로 변환해줌.
- 장점 : 객체지향적 코드로 인해 직관적, 비즈니스 로직에 더 집중할 수 있다.
             재사용 / 유지보수 편리함이 증가한다.
             DB에 대한 종속성이 줄어든다.
- 단점 : 오로지 ORM만으로는 거대한 서비스를 구현하기 힘들다.
             번역기라는 단계가 하나 더 생겼으므로 속도저하가 있다.



## Flask에서 ORM사용하기

- flask에서는 orm을 지원하지 않기 때문에 설치가 필요함.

~~~bash
pip install flask_sqlalchemy
pip install flask_migrate
~~~

- 모듈 import가 필요하다.

~~~python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
~~~



## SQL Alchemy 설정하기

- 앱에 데이터베이스 연결 방법을 알려주자.

~~~python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# True가 기본값, True면 데이터 베이스 객체 수정 및 신호 방출등을 추적함.
# 과다한 메모리를 사용하기 때문에 끔.
~~~



## 초기화하기

~~~python
db = SQLAlchemy(app)
migrate = Migrate(app, db)
~~~



## 테이블 만들기

~~~python
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
~~~



### 만든 테이블 생성(반영)하기

~~~bash
flask db init
flask db migrate
flask db upgrade
~~~



### INSERT

~~~sql
INSERT INTO (username, email)
VALUES ('junho', 'example@gmail.com')
~~~

~~~python
user = User(username = 'junho', email='example@gmail.com')
db.session.add(user)
db.session.commit()
# 반영되게 하기 위해 add, commit
~~~



### SELECT


~~~sql
SELECT * FROM users;
~~~
~~~python
users = User.query.all()
# users는 type list, [<User 'junho'>]라는 객체.
~~~

- ##### WHERE

~~~sql
SELECT * FROM users WHERE username='junho';
~~~
~~~python
users = User.query.filter_by(username='junho').all()
~~~

- ##### LIMIT

~~~sql
SELECT * FROM users WHERE username='junho' LIMIT1;
~~~
~~~python
users = User.query.filter_by(username='junho').first()
~~~

 만약에 없는 값 조회하면 NONE이 리턴됨.

- id값으로 뽑아오기(PK만 get으로 가져올 수 있음)


~~~sql
SELECT * FROM users WHERE id=1;
~~~

~~~python
user = User.query.get(1)
~~~



### LIKE

~~~sql
LIKE
~~~

~~~python
users = User.query.filter(User.email.like('%exam%')).all()
users = User.query.limit(1).offset(2).all()
~~~



### UPDATE

```sql
UPDATE
```

```python
user.query.get(1)
user.username = 'ssafy'
db.session.commit()
user.username
```



### DELETE

```sql
DELETE
```

```python
user = User.query.get(1)
db.session.delete(user)
db.session.commit()
```
