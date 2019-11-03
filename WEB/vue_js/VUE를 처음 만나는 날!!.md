# VUE를 처음 만나는 날!!

## HTML에 VUE를 렌더링 하기

### html에 vue를 연결하기

```html
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
```

대규모 프로젝트를 진행하는 경우,

- cdn 로딩을 해결하기 위해 `npm install vue`를 통해 설치하고
- 로컬에 있는 vue를 로딩하기 위해 다음 코드를 활용할 수 있다.

```html
<script src="nodemodules/vue/dist/vue.js"></script>
```

이제 script에서 vue와 html을 연결하기 위한 작업을 시작해보자.



### 

1. 조건부 렌더링

   v-if : 렌더링 할지말지 자체를 결정

   v-show : 렌더링은 항상 되고 css를 통해 보여질지 숨겨질지를 결정함

2. 리스트 렌더링

   v-for : 동일한 노드에 for와 if가 있다면 우선순위는 for가 높다. 즉 if는 for가 반복될때마다 실행된다.

3. 이벤트리스너

   v-on(약어 `@`) : (전달인자, 수식어) == (keyup, enter)

4. 데이터 바인딩

   v-bind(약어 `:`)

   v-model

5. 렌더링 & 컴파일 관련

   v-pre : 컴파일 하지 않음

   v-once : 처음 단 한번만 렌더링 함

   v-cloak : 컴파일이 완료되면 사라지는 디렉티브

6. template element

   `<template></template>`

   보이지 않는 wrapper 역할을 한다.(hidden wrapper)



computed

미리 계산된 값을 반환한다

template 내에 직접 로직을 넣을 수도 있지만, 그러면 템플릿이 너무 복잡해지기때문에, vue 안에 정의해 두는 것

`{{ newTodo.split().revers }}`이 아니라, 이러한 로직 처리를 computed안에 정의한다.





### 오늘의 질문

??? this