# Django serializer extra field

- django serializer에서 커스텀 필드를 쓰고싶다!
- 그치만 필드가 너무 길어서 일일히 쓰고싶지 않다!
- `__all__`을 쓰고싶다!

```python
class Meta:
    model = Profile
    fields = '__all__'
    extra_fields = ('is_staff', 'similaruser')
```

- fields에는 all값을 주고, extra field에서 추가할 수 있다.

