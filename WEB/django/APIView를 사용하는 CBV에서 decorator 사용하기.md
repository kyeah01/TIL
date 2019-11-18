# APIView를 사용하는 CBV에서 decorator 사용하기

- 사실 아직 해결 못했다. 근데 하고싶어서 일단 마크다운한다.(19.10.28 AM 9:50)

  

## Class 전체에 permission 조건주기

- 이 경우는 간단하다. permission class 를 넣어주기만 하면 된다.

  ```python
  from rest_framework.views import APIView
  from rest_framework.permissions import IsAuthenticated
  
  class SomeThing(APIView):
      permission_classes = (IsAuthenticated,)
  ```

- 이렇게  SomeThing class안의 모든 method에 permission class가 생긴다.



## Method 수준에서의 permission 조건주기

### method_decorator 사용하기

- 401이 아니라 url이 `accounts/login/?next=/`로 바뀌는 방식이다.

  ```python
  from rest_framework.views import APIView
  from django.contrib.auth.decorators import login_required
  from django.utils.decorators import method_decorator
  
  class SomeThing(APIView):
      
      @method_decorator(login_required)
      def get(self, request):
          return Response(status=status.HTTP_200_OK)
  ```

  > 혹시 기본으로 세팅된 LOGIN_URL을 바꾸고싶다면
  >
  > settings.py에
  >
  > ```python
  > LOGIN_URL = '설정하고 싶은 url'
  > ```
  >
  > 를 설정해주면 된다.



### APIView의 method 사용하기

- 답답해서 APIView를 사용하는 restframework의 github를 들어가봤다. 그랬더니 정답인진 모르겠지만, 쓸만한 방법을 찾아냈다.

- APIView는 `permission_denied`라는 method를 제공하는데,  이를 통해 해결할 수 있을 것 같다. 메소드 안에서 해당 method를 요청해서 error를 뿜게 해서 401 error를 띄운다.

  ```python
  def patch(self, request, site_pk):
      self.permission_denied(request)
  	return Response(status=status.HTTP_200_OK)
  ```

- 다른방식도 하나 찾았다!

  ```python
  class SomeThing(APIView):
      
      def has_permission(self, request):
          if request.method in SAFE_METHODS:
              return True
          return request.user == admin
        	# 처음에 obj를 받아서, obj소유자를 확인하는 걸로 변경해도 된다.
          # return obj.owner == request.user 같은식으로.
  
      def get(self, request):
          if not self.has_permission(request):
              return Response(
                  data = {
                      "detail" : "자격 인증데이터(authentication credentials)가 제공되지 않았습니다."
                  }, 
                  status=status.HTTP_401_UNAUTHORIZED)
  
          return Response(status=status.HTTP_200_OK)
  ```

  

