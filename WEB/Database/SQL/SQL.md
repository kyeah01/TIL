# database SQL 기초

- File보다 안전하고 편리하고 빠르게 자료를 보관하기 위해 이용한다.
- SQLite를 사용할 예정, C9에는 자동내장되어있음
- .(dot)로 시작하는 명령어는 실행을 위한 명령어일뿐, SQL문이 아니다.



## 기본 용어 정리

| column | datatype |
| ------ | -------- |
|        |          |

- 스키마 : 데이터 베이스의 구조와 제약조건에 관련된 전반적인 명세를 기술한 것.
- Constraints
  - NOT NULL - 비지 말아야 함(null value를 가질 수 없음.)
  - UNIQUE - 해당 컬럼에서 유일한 값을 가져야 함.
  - PRIMARY KEY - **combination of not null and unique**
  - FOREIGN KEY - 두 테이블을 연결하는데에 사용되는 키.
  - CHECK - 해당 컬럼 값의 범위 설정
  - DEFAULT - null 값을 가지면 defalt값으로 대체함.
  - INDEX - 데이터 검색의 속도향상을 위한 인덱스 설정.



## SQL개념

SQL은 관계형 데이터베이스 관리시스템의 데이터를 관리하기 위해 설계된 특수목적 프로그래밍 언어. 각 테이블은 튜플의 집합이지만 테이블과 쿼리결과는 열의 목록.


1. #### 데이터 정의 언어, DDL :데이터를 정의하기 위한 언어(테이블, 스키마)

   - **CREATE** : 데이터베이스에서 객체(ex. 테이블...)를 생성하는 명령어.

     > CREATE TABLE table_name (field_name INT);

   - **DROP** : 객체 삭제 언어. 롤백복원 불가

     > DROP TABLE table_name;

   - **ALTER** : 객체 구조변경, 현재 테이블에 컬럼추가나 제한 추가(ex null 불가, PK설정 등), ADD, DROP, MODIFY, RENAME

     ADD와 DROP은 CONSTRAINT를 붙여 제약조건을 추가하거나 제거할 수 있다.

     - **ADD** : 컬럼추가, 제약조건 추가

       > ALTER TABLE table_name ADD column_name datatype;

       > ALTER TABLE table_name ADD CONSTRAINT 제약조건명 제약조건;

     - **DROP** : 컬럼제거, 제약조건 제거

       > ALTER TABLE table_name DROP COLUMN column_name;

       > ALTER TABLE table_name DROP CONSTRAINT 제약조건명;

     - **MODIFY** : 컬럼수정

     - **RENAME** : 컬럼명 수정

       > ALTER TABLE table_name RENAME old_column_name TO new_column_name;

   - **TRUNCATE** : 테이블 내의 모든 데이터를 삭제하는 것. 테이블 자체 삭제 아님.(DROP과 구별됨.) 롤백 불가.(DELETE는 가능.)

     > TRUNCATE TABLE table_name;

   
   

2. #### 데이터 조작 언어, DML : 데이터를 저장, 수정, 삭제, 조회등을 하기 위한 언어.

   - **INSERT INTO** : 테이블에 새 레코드 삽입

     > INSERT INTO table_name (column1, column2)
     > VALUES (value1, value2);

   - **UPDATE ~ SET ~ WHERE ~** : 기존 레코드 수정, WHERE 지정하지 않을 시 모든 레코드가 업데이트됨.

     > UPDATE table_name
     > SET column1 = value1, column2 = value2
     > WHERE condition;

   - **DELETE ~ WHERE ~** : 테이블의 기존 레코드 삭제

     > DELETE FROM table_name WHERE condition;

   - **SELECT ~ **

     - **FROM ~** : 데이터 선택에 사용. 리턴된 데이터는 결과세트에 저장됨.

       > SELECT column1, column2 ...
       > FROM table_name;

     - **DISTINCT ~ FROM ~** : 다른 값들만 뽑아내기 위한 명령어(중복값 제외하고 조회). 같은값들은 제외하고 뽑아냄.

       > SELECT DISTINCT column1, column2 ...
       > FROM table_name;

     - **COUNT ~ FROM ~ WHERE ~** : numeric value를 가지는 column의 경우에 사용. AVG, SUM도 마찬가지로 사용 가능.

     - **MIN ~ FROM ~ WHERE ~** : MAX도가능

       > SELECT MIN(column_name)
       >
       > FROM table_name
       >
       > WHERE condition;

   - **WHERE** : 제한조건, address='서울'와 같이 사용. 해당열의 값이 일치하는 레코드만 나타냄. AND나 OR 조건 병행 가능.

   - **LIMIT** : 제한조건, 숫자를 붙여서 나타냄. 2일 경우에 2개 레코드만 나타낸다는 뜻.

   - **OFFSET** : 제한조건, 숫자를 붙여서 나타냄. 2일 경우에 위에서부터 2 이후의 레코드만 나타낸다는 뜻.(3부터 나타냄.)

   - **LIKE** : 제한조건, 패턴매칭으로 나타냄.

     - % - The percent sign represents zero, one, or multiple characters
     - _ - The underscore represents a single character

   - **AUTOINCREMENT**: INTEGER에서만 쓸 수 있음.

   
   

3. #### 데이터 제어 언어, DCL : 데이터 베이스 사용자의 권한제어를 위해 사용되는 언어

   - GRANT, REVOKE, SET TRANSACTION, BEGIN, COMMIT, ROLLBACK, SAVEPOINT, LOCK ... ....



## Hello SQL : table만들기

> 시작하기 전에!
>
> ~~~sql
> > sqlite3
> > .headers on
> > mode column
> > mode csv
> -- 모드 변경을 위해 사용
> ~~~

- csv파일 import 하기

~~~sql
> .import hellodb.csv examples
-- hellodb.csv를 examples로 명명해서 import함

> .tables
-- 테이블 확인 명령어

> .exit
-- sql끄기
~~~



## SQLite3에서 실습하기

- c9에서 flask기반으로 진행.

- tutorial이라는 데이터베이스 생성

~~~bash
sqlite3 tutorial.sqlite3
~~~

- 테이블 생성 후 삭제

~~~sql
.databases
-- 데이터베이스 위치 확인

CREATE TABLE classmates (
    id INT PRIMARY KEY,
    name TEXT
    );
-- 테이블 생성

.tables
-- 테이블 확인

.schema classmates
-- classmate의 schema확인(테이블 생성시 넣은 값)

DROP TABLE classmates;
-- 테이블 삭제
~~~

- 데이터 조작

~~~sql
CREATE TABLE classmates (
    id INT PRIMARY KEY,
    name TEXT,
    age INT,
    address TEXT
    );

.nullvalue “NULL”
-- 값이 없으면 알아서 null value를 넣어주는 명령어

SELECT * FROM classmates;
-- 셀렉해서 보기(확인하기)

.read class_table.sql
-- class_table.sql을 읽어서 실행함.
~~~





#### *Reference*

해피해킹 SQL 교육

위키백과 - SQL

w3cschools

https://hyeonstorage.tistory.com/292