# C9 초기세팅하기

- python 3.6.7버전과 가상환경 구축을 위한 pyenv-virtualenv를 설치하는 경우를 예로 한다. ( python 3.7 버젼은 ubuntu openssl 이슈가 존재한다고 한다. )

- 차례대로 진행하면 된다.



## pyenv

- 파이썬 버전을 관리하는 툴
- 하나의 컴퓨터에 다양한 파이썬 버전을 설치하고 관리한다.

  ~~~bash
  # pyenv 설치
  $ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
  ~~~

  ~~~bash
  # python 설치
  $ pyenv install 3.6.7
  $ pyenv global 3.6.7		# 3.6.7을 글로벌선언
  $ pyenv rehash
  $ python -V					# 설치된 python의 버전 확인
  ~~~

  

## pyenv-virtualenv

- 파이썬 환경을 격리하는 툴로 pyenv의 확장 플러그인이다. 

- 파이썬 버전과 라이브러리의 완전한 격리 환경을 제공한다.

  ~~~bash
  # pyenv-virtualenv 설치
  $ git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
  ~~~

  ~~~bash
  # 가상환경 만들기
  $ pyenv virtualenv <파이썬버전> <가상환경 이름>
  							# (1) 특정 파이썬 버전으로 가상환경 생성하는 경우
  $ pyenv virtualenv <가상환경이름>
  							# (2) 그냥 현재 파이썬 버전으로 생성하는 경우
  
  $ pyenv versions			# pyenv 를 이용해 만든 파이썬 버전들을 출력
  $ pyenv virtualenvs			# 설치된 가상환경 목록만 확인
  ~~~

  ~~~bash
  # global로 가상환경 활성화하기
  $ pyenv activate <가상환경 이름>
  # 활성화되면 커맨드라인 앞에 가상환경 이름이 나옴.
  # 예시) (test37) yourid:~/workspace/ $
  
  # 가상환경 비활성화
  $ pyenv deactivate
  ~~~

  ~~~bash
  # local로 가상환경 활성화하기 : 로컬로 활성화하면 해당 디렉토리 빠져나올 시 자동으로 비활성화된다.
  # 반드시 가상환경으로 지정할 디렉토리로 이동한 후에 활성화시켜야 한다.
  # 현재 디렉토리를 특정 가상환경으로 설정한다는 의미이기 때문이다.
  $ pyenv local <가상환경 이름>
  ~~~

  ~~~bash
  # 가상환경을 완전히 삭제하고 싶다면
  # 이 경우 다시 사용을 위해서는 install이 다시 필요하다
  # 단순히 local과 global을 혼동했다던가 하는 이유로는 deactive만 활용해도 충분하다.
  $ pyenv uninstall <가상환경 이름>
  ~~~



## pip


- 파이썬 라이브러리를 관리한다.

  ~~~bash
  $ pip install --upgrade pip			# 설치와 업그레이드
  $ pip list						# 설치된 파이썬 패키지 목록조회
  ~~~

