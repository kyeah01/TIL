# AWS에 Django server build하기

## 시작하기에 앞서

- [GitHub](<https://github.com/kyeah01/SEMO_Simpl-and-Easy-Manual-Of-API>)의 프로젝트를 aws에 올리려고 한다.
- front는 vue CLI, 백엔드로는 django, DB로는 MySQL을 활용했다.
- DB, backend, front 모두가 하나의 기기가 호스팅하는 1tier방식을 활용하려고 한다.
- front는 아직 올릴 준비가 안됐다고해서 DB와 backend build를 목표로 잡고있다.



## AWS

- 거창하게 서버를 활용한다!가 아니라 가상 컴퓨터에 접속해서 내 프로젝트 파일을 올린다고 생각하면 된다.

- 접속하는 방법은 SSH를 활용하는 방법과 PuTTY를 활용하는 방법 두가지가 존재한다.

  [SSH를 사용하여 Linux 인스턴스에 연결](<https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html>)

  [PuTTY를 사용하여 Windows에서 Linux 인스턴스에 연결](<https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/putty.html>)

- 연결이 완료되었으면 ubuntu의 apt-get을 update 시켜준다.

  ```bash
  $ sudo apt-get update
  ```
  
- 파이썬과 pip, npm을 설치한다.

  ```bash
  $ sudo apt-get install python
  $ sudo apt-get install python-pip
  ```
  
  - python과 pip를 install 하는데 약간의 이슈가 있었다.
  
  - python3버전을 python command로 활용하려고 변경하다보니 이슈가 있었고,
  
  - pip는 그냥 안깔렸다. 아니 사실 깔리긴 했는데 pip command를 찾을 수 없다고 했다.
  
    ```bash
    Traceback (most recent call last):
      File "/usr/bin/pip", line 9, in <module>
        from pip import main
    ModuleNotFoundError: No module named 'pip'
    ```

  - path설정 문제인듯 했다. path 설정하니 해결
  
    [path 설정 참고](<https://inpages.tistory.com/131>)
  
- 프로젝트를 ubuntu에 연동한다. 나는 git의 clone을 사용했다.



## DB연결

- MySQL(8.0.18)를 활용하고 있다.

### MySQL 환경설정

- 설치!!

    ```bash
    $ sudo apt-get install mysql-server
	```

- 외부에서 접속할 수 있게 포트를 열어준다.

    ```bash
    $ sudo ufw allow mysql
    ```

- 그런다음, mysql을 실행하고 서버가 재시작되도 mysql이 자동 시작되도록 등록하자.

    ```bash
    $ sudo systemctl start mysql
    $ sudo systemctl enable mysql
    ```

- mysql 쉘에 들어가서 설치된걸 확인해보자. (초기 비밀번호는 root)
  
    ```bash
    $ sudo /usr/bin/mysql -u root -p
    ```

    ```mysql
    mysql> SHOW VARIABLES LIKE "%version%";
    +-------------------------+-------------------------+
    | Variable_name           | Value                   |
    +-------------------------+-------------------------+
    | innodb_version          | 5.7.27                  |
    | protocol_version        | 10                      |
    | slave_type_conversions  |                         |
    | tls_version             | TLSv1,TLSv1.1           |
    | version                 | 5.7.27-0ubuntu0.18.04.1 |
    | version_comment         | (Ubuntu)                |
    | version_compile_machine | x86_64                  |
    | version_compile_os      | Linux                   |
    +-------------------------+-------------------------+
    8 rows in set (0.01 sec)
    ```

- 초기 비밀번호 변경

    ```mysql
    ALTER USER 'root'@'localhost' IDENTIFIED BY 'your_password'
    ```




### database 생성

- database를 생성하자

  ```mysql
  CREATE DATABASE your_db_name;
  ```

- 만들어진 database를 확인하자

  ```mysql
  mysql> SHOW DATABASES;
  +--------------------+
  | Database           |
  +--------------------+
  | information_schema |
  | your_database_name |
  | mysql              |
  | performance_schema |
  | sys                |
  +--------------------+
  5 rows in set (0.00 sec)
  ```

  

### host를 설정하자

- 현재 유저와 host를 확인한다.

  ```bash
  mysql> SELECT User, Host, authentication_string FROM mysql.user;
  +------------------+-----------+-------------------------------------------+
  | User             | Host      | authentication_string                     |
  +------------------+-----------+-------------------------------------------+
  | root             | localhost |                                           |
  | mysql.session    | localhost | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE |
  | mysql.sys        | localhost | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE |
  | debian-sys-maint | localhost | *BDB729D8CBE6184E0247724ADD7212861269927F |
  +------------------+-----------+-------------------------------------------+
  4 rows in set (0.00 sec)
  ```

- 만든 DB에 붙을 수 있는 user를 생성한다.

  ```mysql
  mysql> CREATE USER 'semo'@'your_name' IDENTIFIED BY 'your_password';
  Query OK, 0 rows affected (0.01 sec)
  
  mysql> FLUSH PRIVILEGES;
  Query OK, 0 rows affected (0.00 sec)
  ```

- 계정이 잘 생성되었는지 다시 user table을 확인한다.

  ```mysql
  mysql> SELECT User, Host, authentication_string FROM mysql.user;
  +------------------+-----------+-------------------------------------------+
  | User             | Host      | authentication_string                     |
  +------------------+-----------+-------------------------------------------+
  | root             | localhost |                                           |
  | mysql.session    | localhost | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE |
  | mysql.sys        | localhost | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE |
  | debian-sys-maint | localhost | *BDB729D8CBE6184E0247724ADD7212861269927F |
  | semo             | localhost | *2735CBBFEFEC4F6B8808BB665EDB208675FA27CC |
  +------------------+-----------+-------------------------------------------+
  5 rows in set (0.00 sec)
  ```

- 이제 생성한 계정에 DB 접근 권한을 부여합니다.

  ```mysql
  mysql> GRANT ALL PRIVILEGES ON your_db_name.* to your_name@localhost;
  Query OK, 0 rows affected (0.00 sec)
  
  mysql> FLUSH PRIVILEGES;
  Query OK, 0 rows affected (0.00 sec)
  ```

- 해당 계정의 GRANT 권한을 확인합니다.

  ```mysql
  mysql> SHOW GRANTS FOR 'your_name'@'localhost';
  +-----------------------------------------------------------------------+
  | Grants for your_name@localhost                                        |
  +-----------------------------------------------------------------------+
  | GRANT USAGE ON *.* TO 'your_name'@'localhost'                         |
  | GRANT ALL PRIVILEGES ON `your_db_name`.* TO 'your_name'@'localhost'   |
  +-----------------------------------------------------------------------+
  2 rows in set (0.00 sec)
  ```

- GRANT ALL PRIVILEGES ON `your_db_name`.* TO 'your_name'@'localhost'을 확인했으니 이제 완료되었다!

- 다른 PC에서 해당 DB에 접근하고 싶다면, 아래 명령을 활용한다.

  ```mysql
  CREATE USER 'root'@'your_ip_address' IDENTIFIED BY 'your_password';
  GRANT ALL PRIVILEGES ON * . * TO 'root'@'your_ip_address' WITH GRANT OPTION;
  FLUSH PRIVILEGES;
  ```



## Django deploy

- django를 deploy 하기 위해 개발환경과 프로덕션 환경에 대한 설정을 분리해야 한다.

### settings.py 분할

settings.py를 하나의 폴더로 구성해서 분할한다.

- 분할하지 않아도 된다. 나는 deploy 환경과 develop 환경, local 환경을 각각

  |       | deploy | develop | local |
  | ----- | ------ | ------- | ----- |
  | MySQL | O      | O       | X     |
  | DeBug | X      | O       | O     |

  처럼 분할하기 위해 settings.py를 세단계로 분리했다.

- 분할하는 방법은 간단하다. settings.py를 setting dir로 변경한 다음, 하위에 `__init__.py`, `base.py`, 만들고 싶은 환경 이름 으로 된 python 파일을 생성하면 된다.

- 그런다음 `base.py`에 원래의 settings.py에 들어갔던 내용을 넣고, 각각 다르게 설정하고 싶은 내용만 분할해서 각각의 환경이름으로 된 python 파일에 넣어준다.

- 그러면 다음과 같은 파일구조가 된다.

  ```markdown
  project_name/
  	project_name/
  		settings
  			__init__.py
  			base.py
          	local.pyt
          	develop.py
  ```
  
- 자세한 내용은 [GitHub](https://github.com/kyeah01/TIL/blob/master/WEB/django/Django Settings.py 분리하기.md)참고

### 환경설정

미리 만들어두었던 requirements.txt를 install시켜준다.

```bash
$ pip install -r requirements.txt
```

- 여기서 이슈가 발생했다. `mysqlclient` 패키지가 MySQL을 찾지 못해서 설치 할 수 없다는 에러다.

  ```bash
  Complete output from command python setup.py egg_info:
  /bin/sh: 1: mysql_config: not found
  /bin/sh: 1: mariadb_config: not found
  /bin/sh: 1: mysql_config: not found
  Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/tmp/pip-build-6gqmrlxd/mysqlclient/setup.py", line 16, in <module>
  metadata, options = get_config()
  File "/tmp/pip-build-6gqmrlxd/mysqlclient/setup_posix.py", line 61, in get_config
  libs = mysql_config("libs")
  File "/tmp/pip-build-6gqmrlxd/mysqlclient/setup_posix.py", line 29, in mysql_config
  raise EnvironmentError("%s not found" % (_mysql_config_path,))
  OSError: mysql_config not found
  ```

- 이를 해결하기 위해 mysql을 다시 깔고, mysql client를 깔고, 별 짓을 다했으나 해결이 안됐다. 해결하기 위해서는 추가 패키지를 설치해야 한다.

  ```bash
  $ sudo apt-get install libmysqlclient-dev
  ```

- 그럼 깔끔하게 해결!

- 이제 장고 서버를 돌릴 수 있다.

  ```bash
  $ python manage.py runserver --settings=myapp.settings.production &
  ```

  (뒤의 &은 bash창이 꺼져도 서버가 꺼지지 않게 하는 nohup설정이다.)