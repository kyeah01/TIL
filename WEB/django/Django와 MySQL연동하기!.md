# Django와 MySQL연동하기!

- 이 과정에서 가장 힘들었던 건 MySQL 설치과정이다.
- 그러니 이미 설치하고오신분들은 안심하셔도 될듯



## MySQL 설치하기

- <https://dog-developers.tistory.com/20>

- <https://all-record.tistory.com/93>

- 참고로 나는 이 과정에서 connector/python이 설치 fail이 떴다.

  -> 당황했는데 그냥 무시하고 했더니 됐다. django와 연동하는데는 그렇게 큰 의미 없는듯.



## MySQL Workbench

- shell에선 하시는 분들 많이봤는데, 워크벤치는 없어서 애먹었다.

- 거기다 shell에서 왠지는 몰라도 내 명령어를 신택스 에러로 다 리젝하는 바람에 그냥 워크벤치로 하기로 결정!

- 먼저 데이터베이스를 생성해야 한다.

  ```mysql
  CREATE DATABASE databasename;
  ```

- 그런다음 GRANT과정만 거치면 된다.

  `server` > `Users and Privileges` 로 들어간다.

- 하단의 `Add Account`를 누른 다음, login Name과 password를 정해 넣는다.

  ![1571967178193](https://user-images.githubusercontent.com/45934061/67536706-6efca080-f713-11e9-8335-1b94f97080ed.png)

- 모든 ip에서 접근을 허용하고 싶다면 `%`, 아니라면 대역을 정해 정의한다.



## 연동하기

-  Django와 MySQL을 연결하는데 도움을 줄 `mysqlclient`를 설치한다.

   ```
   $ pip install mysqlclient
   ```

- settings.py

  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': '아까 설정했던 DB이름',
          'USER': '호스트 설정했던 유저이름',
          'PASSWORD': MYSQL_SECRET_KEY,
          'HOST': '호스트할 ip주소',
          'PORT': '처음에 mysql깔때 넣었던 포트주소, default값은 3306',
      }
  }
  ```



이제 `python manage.py migrate`를 해주면 완성이다.