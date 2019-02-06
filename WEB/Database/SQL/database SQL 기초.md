flask에서 python기반으로 데이터 주고받기

1. html을 python에서 열기 위해서 render_templates를 활용할 예정이다.





# database SQL 기초

- File보다 안전하고 편리하고 빠르게 자료를 보관하기 위해 이용한다.
- SQLite를 사용할 예정, C9에는 자동내장되어있음



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

1. 데이터 정의 언어, DDL :데이터를 정의하기 위한 언어(테이블, 스키마)

   - CREATE : 데이터베이스에서 객체(ex. 테이블...)를 생성하는 명령어.

     > CREATE TABLE table_name (field_name INT);

   - DROP : 객체 삭제 언어. 롤백복원 불가

     > DROP TABLE table_name;

   - ALTER : 객체 구조변경, 현재 테이블에 컬럼추가나 제한 추가(ex null 불가, PK설정 등), ADD, DROP, MODIFY, RENAME

     ADD와 DROP은 CONSTRAINT를 붙여 제약조건을 추가하거나 제거할 수 있다.

     - ADD : 컬럼추가, 제약조건 추가

       > ALTER TABLE table_name ADD column_name datatype;

       > ALTER TABLE table_name ADD CONSTRAINT 제약조건명 제약조건;

     - DROP : 컬럼제거, 제약조건 제거

       > ALTER TABLE table_name DROP COLUMN column_name;

       > ALTER TABLE table_name DROP CONSTRAINT 제약조건명;

     - MODIFY : 컬럼수정

     - RENAME : 컬럼명 수정

       > ALTER TABLE table_name RENAME old_column_name TO new_column_name;

   - TRUNCATE : 테이블 내의 모든 데이터를 삭제하는 것. 테이블 자체 삭제 아님.(DROP과 구별됨.) 롤백 불가.(DELETE는 가능.)

     > TRUNCATE TABLE table_name;

2. 데이터 조작 언어, DML : 데이터를 저장, 수정, 삭제, 조회등을 하기 위한 언어.

   - INSERT INTO : 테이블에 새 레코드 삽입

     > INSERT INTO table_name (column1, column2)
     > VALUES (value1, value2);

   - UPDATE ~ SET ~ WHERE ~ : 기존 레코드 수정, WHERE 지정하지 않을 시 모든 레코드가 업데이트됨.

     > UPDATE table_name
     > SET column1 = value1, column2 = value2
     > WHERE condition;

   - DELETE : 테이블의 기존 레코드 삭제

     > DELETE FROM table_name WHERE condition;

   - SELECT ~ FROM ~ : 데이터 선택에 사용. 리턴된 데이터는 결과세트에 저장됨.

     > SELECT column1, column2 ...
     > FROM table_name;

3. 데이터 제어 언어, DCL : 데이터 베이스 사용자의 권한제어를 위해 사용되는 언어

   - GRANT, REVOKE, SET TRANSACTION, BEGIN, COMMIT, ROLLBACK, SAVEPOINT, LOCK ... ....



## Hello SQL : table만들기

> 시작하기 전에!
>
> ~~~sqlite
> > sqlite3
> > .headers on
> > mode column
> > mode csv
> -- 모드 변경을 위해 사용
> ~~~

- csv파일 import 하기

~~~sqlite
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

~~~sqlite
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

- 

~~~sqlite
CREATE TABLE classmates (
    id INT PRIMARY KEY,
    name TEXT,
    age INT,
    address TEXT
    );

SELECT * FROM classmates;
-- 셀렉해서 보기(확인하기)

.read class_table.sql
-- class_table.sql을 읽어서 실행함.
~~~


sqlite> .tables
sqlite> .read class_table.ql

sqlite> .tables
classmate
sqlite> schema classmates;
Error: near "schema": syntax error
sqlite> .schema classmates
sqlite> .headers on
sqlite> .mode column
sqlite> .read insert.sql

sqlite> SELECT * FROM classmate
   ...> ;
id          name        age         address
----------  ----------  ----------  ----------
            홍길동   23
sqlite> .read insert.sql

Error: incomplete SQL: INSERT INTO classmate (id, name, age, address)
VALUES(2, '홍길동', 30, '서울')
sqlite> .read insert.sql

sqlite> SELECT
   ...> * FROM classmate
   ...> ;
id          name        age         address
----------  ----------  ----------  ----------
            홍길동   23
2           홍길동   30          서울
sqlite> DROP TABLE classmate;
sqlite> .tables
sqlite> .table
sqlite> .read create_table.sql

sqlite> .read create_table.sql
Error: near line 1: table classmate already exists

sqlite> .read insert.sql
Error: near line 8: NOT NULL constraint failed: classmate.address

Error: incomplete SQL: INSERT INTO classmate (name, age)
VALUES('신채원', 15)
INSERT INTO classmate (name, age)
VALUES('박수현', 5)
sqlite> SELECT * FROM classmate;
sqlite> .read insert.sql
Error: near line 8: 3 values for 2 columns
Error: near line 10: 3 values for 2 columns

sqlite> .read insert.sql

sqlite> SELECT * FROM classmates
   ...> ;
Error: no such table: classmates
sqlite> SELECT * FROM classmate;
id          name        age         address
----------  ----------  ----------  ----------
1           안상현   43          대전
2           신채원   15          서울
sqlite> .read insert.sql

sqlite> SELECT * FROM classmate;
id          name        age         address
----------  ----------  ----------  ----------
1           안상현   43          대전
2           신채원   15          서울
3           안상현   43          대전
4           신채원   15          서울
sqlite> SELECT id, name FROM classmate;
id          name
----------  ----------
1           안상현
2           신채원
3           안상현
4           신채원
sqlite>
sqlite>
sqlite> SELECT id, name FROM classmate LIMIT 2;
id          name
----------  ----------
1           안상현
2           신채원
sqlite>
sqlite> SELECT * FROM classmate LIMIT 1 OFFSET 2;
id          name        age         address
----------  ----------  ----------  ----------
3           안상현   43          대전
sqlite> SELECT * FROM classmate WHERE address='서울'
   ...> ;
id          name        age         address
----------  ----------  ----------  ----------
2           신채원   15          서울
4           신채원   15          서울
sqlite> SELECT * FROM classmate WHERE id=2;
id          name        age         address
----------  ----------  ----------  ----------
2           신채원   15          서울
sqlite>
sqlite> SELECT name FROM classmate WHERE address='서울';
name
----------
신채원
신채원
sqlite> .read delete.sql

sqlite> SELECT * FROM classmate;
id          name        age         address
----------  ----------  ----------  ----------
1           안상현   43          대전
2           신채원   15          서울
4           신채원   15          서울
sqlite> .read update.sql

sqlite> SELECT * FROM classmate;
id          name        age         address   

----------  ----------  ----------  ----------
1           안상현   43          대전    
2           신채원   15          서울    
4           강예원   15          제주    
sqlite> SELECT * FROM classmate;
id          name        age         address   
----------  ----------  ----------  ----------
1           안상현   43          대전    
2           신채원   15          서울    
4           강예원   15          제주    
sqlite> .read update.sql                                                                         

sqlite> SELECT * FROM classmate;
id          name        age         address   
----------  ----------  ----------  ----------
1           안상현   43          대전    
2           신채원   15          서울    
4           박성주   15          제주    
sqlite> 





sqlite> SELECT age FROM classmate
   ...> ;
age       
----------
43        
15        
15        
sqlite> SELECT DISTINCT age FROM classmate;

age       
----------
43        
15        

중복값 제거하고 조회



DROP TABLE users;

SELECT COUNT(*) FROM users;

SELECT AVG(age) FROM users WHERE age >= 30;

SELECT first_name, MAX(balance) FROM users;

LIKE는 정확한 값이 아니라 패턴을 반환함.









#### *Reference*

해피해킹 SQL 교육

위키백과 - SQL

https://hyeonstorage.tistory.com/292