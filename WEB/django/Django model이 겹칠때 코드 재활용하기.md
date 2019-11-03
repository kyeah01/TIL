# Django model이 겹칠때 코드 재활용하기

## 문제점

- 비슷한 필드를 가지는 model을 두개 정의하는데 똑같은 필드를 여러번 정의하고싶지않다!



## 해결방법

- class based로 model을 정의하니 상속을 이용하자!!



### code

```python
class MotherModel(models.Model):
    title = models.CharField(max_length=100)
    
    class Meta:
        abstract = True
    
class FirstChildrenModel(MotherModel):
    content = models.TextField()
    
class SecondChildrneModel(MotherModel):
    comment = models.TextField()
```

- mother model은 실제로 생성되지 않는다.
- first children model과 second children model이 실제로 생성된다.
- 각 모델은 다음과 같은 구조를 가진다.
  - first children model
    - title
    - content
  - second children model
    - title
    - comment