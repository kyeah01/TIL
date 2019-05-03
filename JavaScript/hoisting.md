# JS hoisting

`var` : 함수스코프 () - 함수 바깥으로 나가면 알아볼 수 없음.

`let` : 블록스코프 {}

### let은 블록스코프

```javascript
{
    let x = '정운지'
    console.log(x)          // 정운지
    {
        let x = 1
        console.log(x)      // 1
    }
    console.log(x)          // 정운지
}
console.log(typeof x)       // undefined
```

- 만약 var로 선언했을 경우, 출력값은 정운지, 1, 1, number가 나오게 된다.
- 이를 전역변수의 오염이라고 한다.
- var로 선언하면, 현재 스코프(유효범위) 안이라면 어디든지 사용할 수 있으며, 심지어 선언하기도 전에 사용할 수 있다.
- 



