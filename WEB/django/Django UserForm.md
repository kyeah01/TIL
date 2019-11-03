# User Authentication in Django

## Model

### User Model

- 장고의 유저모델은 구현할 필요가 없다!!
  이미 구현되어있기때문에 import 하기만 하면 된다.

```python
from django.contrib.auth.models import User
```

```python
from django.contrib.auth import get_user_model
```

- User 모델이 아니라 get_user_model을 사용하는 것이 바람직하다.
  ([django : User 모델이 아니라 get_user_model을 사용해야 하는 이유](https://docs.djangoproject.com/ko/2.1/topics/auth/customizing/#referencing-the-user-model))

### Log In

- 로그인을 받을 폼

```python
from django.contrib.auth.form import AuthenticationForm
```

- 실제로 로그인을 수행하는 model

```python
from django.contrib.auth import login
```





### Signup

- CRUD의 create와 비슷함.

- Class User & get user model이 이미 정의되어있고, import해서 사용하기만 하면 된다.
  (또한 관리 툴도 이미 구현되어있다...! 장고 최고야)

- 유저를 가입시키기 위한 Form 또한 이미 구현되어있다. 마찬가지로 정의할 필요가 없다.

- custom해서 쓰고 싶다면, 해당 model form을 상속해서 구현할 수 있다.

  ```python
  from django.forms import ModelForm
  ```



### Login

- Create a Session하는 과정.

  : Session = 브라우저의 어떤 정보를 서버가 임시로 들고있는 것. 우리는 user가 누구인지 구분하기 위해 사용한다. (http는 저장이 불가능하다.)

- 

  

  

  이 세션은 사용자가 로그인하면 로그인한 사용자의 정보를 페이지가 전환되더라도 계속 가지고있다.

로그아웃 버튼을 누르거나, 세션이 만료(만료시간이 지정되어잇다고 하면)되면 이 정보를 드랍한다.

-> 한마디로 세션관리를 하지 않아도 된다.

