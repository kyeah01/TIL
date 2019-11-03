# 장고에서 migrations자체를 날려버리고 싶을때

1. migration폴더를 `__init__`만 남기고 삭제한다.

2. database 에 접속해서 테이블 중 `django_migrations` 라는 테이블에서 해당 앱에 대한 row를 삭제해야한다.

   ~~~sqlite
   DELETE FROM django_migrations WHERE app = '앱 이름'
   ~~~

   

##### refenrence

https://forybm.tistory.com/2