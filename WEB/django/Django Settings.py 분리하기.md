# Django Settings.py 분리하기

>  django에 MySQL을 사용하면서, deploy를 진행하면서 local setting과 production setting을 분할해 사용할 필요성이 생겼다. settings.py 파일을 분할해서 사용하면 `if DEBUG`, `if not DEBUG` 같은 조건문을 사용하지 않고 세팅 조건을 나눌 수 있기 때문에, settings.py를 분할하기로 마음먹었다.



## Settings.py 파일을 분리하자.

settings.py를 하나의 폴더로 구성해서 분할한다.

- 분할하지 않아도 된다. 나는 deploy 환경과 develop 환경, local 환경을 각각

  |       | deploy | develop | local |
  | ----- | ------ | ------- | ----- |
  | MySQL | O      | O       | X     |
  | DeBug | X      | O       | O     |

  처럼 분할하기 위해 settings.py를 세단계로 분리했다.

- settings.py를 setting dir로 변경한 다음, 하위에 `__init__.py`, `base.py`, 만들고 싶은 환경 이름 으로 된 python 파일을 생성하면 된다. (원래 `settings.py`위치에 `settings` 폴더가 들어간다고 생각하면 된다.)

  ```markdown
  project_name/
  	project_name/
  		__init__.py
  		urls.py
  		wsgi.py
  		settings
  			__init__.py
  			base.py
          	local.pyt
          	develop.py
  ```

### base.py

- 원래 `settings.py`안의 내용을 모두 `base.py`에 넣는다. 분리하려고 하는 환경설정은 뺀다.

- `local.py`

  ```python
  import os
  import string, random
  from backend.settings.base import *
  
  DEBUG = True
  ALLOWED_HOSTS = []
  chars = ''.join([string.ascii_letters, string.digits, string.punctuation]).replace('\'', '').replace('"', '').replace('\\', '')
  
  SECRET_KEY = ''.join([random.SystemRandom().choice(chars) for i in range(50)])
  
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
      }
  }
  ```

- `develop.py`

  ```python
  from backend.settings.base import *
  import os, json
  
  DEBUG = True
  ALLOWED_HOSTS = []
  
  secret_file = os.path.join(BASE_DIR, 'secret.json')
  
  with open(secret_file) as f:
      secrets = json.loads(f.read())
  
  # SECURITY WARNING: keep the secret key used in production secret!
  SECRET_KEY = secrets.get("DJANGO_SECRET")
  
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': secrets.get("MYSQL_DB_NAME"),
          'USER': secrets.get("MYSQL_USER"),
          'PASSWORD': secrets.get("MYSQL_SECRET"),
          'HOST': secrets.get("MYSQL_HOST"),
          'PORT': secrets.get("MYSQL_PORT"),
      }
  }
  ```

- `production.py`

  ```python
  from backend.settings.base import *
  import os, json
  
  DEBUG = False
  ALLOWED_HOSTS = ['*']
  
  secret_file = '/etc/secret.json'
  
  with open(secret_file) as f:
      secrets = json.loads(f.read())
  
  SECRET_KEY = secrets.get("DJANGO_SECRET")
  
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': secrets.get("MYSQL_DB_NAME"),
          'USER': secrets.get("MYSQL_USER"),
          'PASSWORD': secrets.get("MYSQL_SECRET"),
          'HOST': secrets.get("MYSQL_HOST"),
          'PORT': secrets.get("MYSQL_PORT"),
      }
  }
  ```

  