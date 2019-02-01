flask에서 python기반으로 데이터 주고받기

1. html을 python에서 열기 위해서 render_templates를 활용할 예정이다.





# database SQL 기초

- File보다 안전하고 편리하고 빠르게 자료를 보관하기 위해 이용한다.

- SQLite를 사용할 예정, C9에는 자동내장되어있음

## 기본 용어 정리

### 1. 스키마

| colume | datatype |
| ------ | -------- |
|        |          |

- 데이터 베이스의 구조와 제약조건에 관련된 전반적인 명세를 기술한 것.

- PK(기본키) : Primary Key. 각 행, 레코드의 고유값으로 반드시 설정하여야 하며 데이터 베이스 관리 매치 관계 설정시 유용하게 사용된다. 절대 겹치면 안된다.

### 2. SQL개념

1. DDL :데이터를 정의하기 위한 언어(테이블, 스키마)
2. DML : 데이터를 저장, 수정, 삭제, 조회등을 하기 위한 언어.
3. DCL : 데이터 베이스 사용자의 권한제어를 위해 사용되는 언어

### 3. Hello SQL : table만들기

> 시작하기 전에!
>
> ~~~sqlite
> > sqlite3
> > .headers on
> > mode column
> > mode csv
> -- 모드 변경을 위해 사용
> ~~~

1. csv파일 import 하기

   ~~~sqlite
   > .import hellodb.csv examples
   -- hellodb.csv를 examples로 명명해서 import함
   > .tables
   -- 테이블 확인 명령어
   > .exit
   -- sql끄기
   ~~~



## Database 만들기

### 1. database 만들기





sqlite3 tutorial.sqlite3
SQLite version 3.8.2 2013-12-06 14:53:30
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> .databases
seq  name             file

---  ---------------  ----------------------------------------------------------
0    main             /home/ubuntu/workspace/tutorial.sqlite3
sqlite> CREATE TABLE classmates (
   ...> id INT PRIMARY KEY,
   ...> name TEXT
   ...> );
sqlite> .tables
classmates
sqlite> .schema tablemates
sqlite> .schema classmates
CREATE TABLE classmates (
id INT PRIMARY KEY,
name TEXT
);
sqlite> DROP TABLE classmates;
sqlite> .tables
sqlite> .database
seq  name             file

---  ---------------  ----------------------------------------------------------
0    main             /home/ubuntu/workspace/tutorial.sqlite3
1    temp
sqlite> CREATE TABLE classmate (
   ...> id INT PRIMARY KEY,
   ...> name TEXT,
   ...> age INT,
   ...> address TEXT
   ...> );
sqlite> .tables
classmate
sqlite> SELECT * FROM classmates
   ...>
   ...>
   ...>
   ...>
   ...> ;
Error: no such table: classmates
sqlite> .schema classmates
sqlite> .schema classmate
CREATE TABLE classmate (
id INT PRIMARY KEY,
name TEXT,
age INT,
address TEXT
);
sqlite> DROP TABLE classmate
   ...> ;
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