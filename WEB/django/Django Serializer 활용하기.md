# Django Serializer

- 편할려고 쓰는거다. 쓰면 무지막지하게 편해지니까.
- 그냥 form이나 modelform으로 대체할 수도 있다. 그치만 serializer가 훨씬 편하고, 안정적이다.
- django rest frameowrk docs에서는 serializer를 복잡한 데이터를 파이썬 데이터 유형으로 변환해주고, 다시 다른 데이터 유형(JSON, XML 등)으로 변환해주는 역할으로 정의한다.
- 여기서는 ModelSerializer를 소개한다.



## serializers.py

- 가장 빠르고 쉽게 정의하자.

  ```python
  from rest_framework import serializers
  from .models import APISite
  
  class APISiteDetailSerializer(serializers.ModelSerializer):
      class Meta:
          model = APISite
          fields = '__all__'
  ```

- 어떤 model을 사용하는 serializer인지를 쓰고, fields는 model의 field중에 쓰고 싶은 것을 쓰고, 모든것을 다 사용하고싶다면 `'__all__'`을 사용한다.



## methodField

- 모델에는 없지만 serializer로는 리턴해주고 싶은 field가 있을때, 사용하는 field다.

  ```python
  from rest_framework import serializers
  from .models import APISite
  
  class APISiteDetailSerializer(serializers.ModelSerializer):
      customfield = serializers.SerializerMethodField('get_custom')
      class Meta:
          model = APISite
          fields = '__all__'
          extra_fields = ()
         
     	def get_custom(self, obj):
          return '1'
  ```

  

## CRUD

### Create

```python
def post(self, request):
    serializer = APISiteDetailSerializer(request.data)	# 1
    if serializer.is_valid():							# 2
        serializer.save()								# 3
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

- #1 : serializer에 넣어주려고 하는 정보를 넣어준다. post로 요청을 받는 경우는 request.data에 해당 정보가 들어있기 때문에 `APISiteDetailSerializer(request.data)`
- #2 : `is_valid` 처리를 통해 data 검증을 한다.
- #3 : 검증된 데이터를 save한다. 이 과정에서 덧붙이고싶은 내용이 있다면, save의 인자로 줘서 해결할 수 있다.



### Read

```python
def get(self, request, site_pk):
    apiSite = get_object_or_404(APISite, pk=site_pk)		#1
    serializer = APISiteDetailSerializer(apiSite)			#2
    return Response(serializer.data, status=status.HTTP_200_OK)
```

- #1 : 읽어올 인스턴스를 가져온다.
- #2 : 인스턴스를 serializer에 넣어 변환한다.



### Update

#### PATCH : 부분수정

```python
def patch(self, request, site_pk):
    apiSite = get_object_or_404(APISite, pk=site_pk)			#1
    serializer = APISiteDetailSerializer(instance=apiSite, data=request.data, partial=True)													#2
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

- #1 : 읽어올 인스턴스를 가져온다.
- #2 : 시리얼라이저에 인스턴스를 넣어주고, 수정에 해당하는 데이터를 넣어준다. partial True를 설정해서 부분수정임을 명시해준다.
- #3 : 검증과정을 거친다음,
- #4 : 저장한다. 마찬가지로 이 과정에서 덧붙이고싶은 내용이 있다면, save의 인자로 줘서 해결할 수 있다.



#### PUT : 전체수정

```python
def patch(self, request, site_pk):
    apiSite = get_object_or_404(APISite, pk=site_pk)
    serializer = APISiteDetailSerializer(instance=apiSite, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

- 다른부분은 동일, partial True를 해제한다.



### Delete

```python
def delete(self, request, site_pk):
    apiSite = get_object_or_404(APISite, pk=site_pk)		#1
    apiSite.delete()										#2
    return Response(status=status.HTTP_204_NO_CONTENT)
```

- #1 : 삭제하려고 하는 인스턴스를 들고온다.
- #2 : delete선언.