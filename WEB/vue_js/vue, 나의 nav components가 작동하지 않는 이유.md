# vue, 나의 nav components가 작동하지 않는 이유

## error

`error: The "nav" component has been registered but not used (vue/no-unused-components) at src\App.vue:13:5:`



## 이유

- 결론부터 말하자면 nav라는 기본 elements가 이미 존재하기 때문이다.
- 그걸 몰라서 고생을 했다ㅠ
- div라는 이름의 컴포넌트를 정의하고 import하는 거랑 똑같다!



## 해결방법

- 컴포넌트 이름을 nav가 아닌 거로 바꿔주면 완료!!