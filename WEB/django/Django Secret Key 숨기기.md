# Django Secret Key 숨기기

- django는 secret key를 가진다!

  settings.py에 있는 `SECRET_KEY`친구가 바로 그 친구!!

  이 친구를 숨기지 않으면 django의 보안기능이 사라질 위험이 있다.

- 컴퓨터 환경변수에 숨겨서 로드하는 방식도 있지만, 팀간 키 공유를 편리하게 하기 위해 새로운 파일에서 로드하고, gitignore를 통해 해당 파일을 숨기는 식으로 공유하고자 한다.



## JSON file

- 우선 json file을 생성한다. (이름은 맘대로) secret.json으로 하나 만들었다.

  ```json
  {
      "DJANGO_SECRET":'숨기고 싶은 키',
      "MYSQL_SECRET":'숨기고 싶은 키'
  }
  ```

- django project가 있는 파일위치에 놓고 쓰자.(그래야 편하니까)

  그래서 최종 위치는 `django_project_file` > `secret.json`



## Settings.py

- 이제 setting에 들어갈 token들이 다 숨겨졌다. 로드하는 과정을 거치면 된다.

  ```python
  import os, json
  from django.core.exceptions import ImproperlyConfigured
  
  BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  
  secret_file = os.path.join(BASE_DIR, 'secret.json')
  
  with open(secret_file) as f:
      secrets = json.loads(f.read())
  
  def get_secret(setting, secrets=secrets):
      """비밀 변수를 가져오거나 명시적 예외를 반환한다."""
      try:
          return secrets[setting]
      except KeyError:
          error_msg = "Set the {} environment variable".format(setting)
          raise ImproperlyConfigured(error_msg)
  
  DJANGO_SECRET_KEY = get_secret("DJANGO_SECRET")
  MYSQL_SECRET_KEY = get_secret("MYSQL_SECRET")
  ```

- `DJANGO_SECRET_KEY`와 `MYSQL_SECRET_KEY`에 키가 잘 로드되었으니, 원래 넣어야 했던 자리에 해당 변수를 넣어주면 로드과정은 끝이 난다!



## .gitignore

- 이제 해당 키가 git에 올라가지 않게 숨겨야 한다.

- `.gitignore`파일을 켜서 

  ```markdown
  ### secret key ###
  secret.json
  ```

  를 추가해주면 진짜 끝이다!
  
- 이제 팀원들에게 secret.json을 공유해주면 된다!



##### 참고자료

<https://wayhome25.github.io/django/2017/07/11/django-settings-secret-key/>

  