# MongoDB - Django

> 2019.10.17
>
> django와 mongoDB를 연결하는것을 목표로 합니다.
>
> 
>
> 프로그램	버전
> Django		2.2.4
> djongo		1.2.36
> mongoDB	4.2



## Installation

### MongoDB

- [다운로드 경로][https://www.mongodb.com/download-center]
  윈도우의 경우 msi버전 설치.

- 시스템 환경변수 설정을 해야 cmd나 bash창에서 mongo 명령어를 사용할 수 있으므로 

  `mongoDB_설치된_절대경로\bin`

  을 시스템 변수의 Path에 등록합니다.

### Djongo

```bash
$ pip install djongo
```



## HOST setting

> 프로젝트 진행 시 여러개의 DB를 빌드하는 것이 아니라 하나의 컴퓨터에서 호스팅해서 다른 컴퓨터에서 접근할 수 있게 하기 위해서 네트워크 호스트를 설정해줍니다.

- mongoDB 설치 파일 중 `bin` > `mongod.cfg`파일을 켜 수정합니다.

  ```text
  net:
    port: `원하는_포트`
    bindIp: `ipv6 주소`
  ```

- 그런다음 윈도우 서비스에 들어가서  MongoDB Server를 재시작합니다.

![윈도우 서비스](https://user-images.githubusercontent.com/45934061/67002798-9c47be00-f117-11e9-9055-fa464978855c.png)





<div style="text-align:center"><b>이제 mongoDB를 django에 설치하기 위한 사전작업이 모두 끝났습니다.</b><div>



## Django와 MongoDB를 연결하자

- `settings.py`에 설정을 추가하면됩니다

  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'djongo',
          'NAME': 'api-djongo-db',
          'HOST': '192.168.31.52',
          'PORT': 8080,
      }
  }
  ```

  설정이 모두 끝났습니다.