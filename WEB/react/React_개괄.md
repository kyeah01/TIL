# React

## 개략

- 리액트는 자바스크립트의 라이브러리
- Change Effect // Transition : 
   버츄얼돔을 만들어놓고 정보가 변경될때마다 컴포넌트를 갈아끼는 방식.



### 기본 세팅

- react 설치

  ```bash
  $ npm i -g create-react-app
  ```
  
- 프로젝트 생성

  ```bash
  $ create-react-app your_app_name
  ```

  - app name에 대문자는 들어갈 수 없다.
    (그래서 camelCase는 불가함.)

- 서버 구동

  ```bash
  $ npm run start
  ```



> #### WebPack
>
> ```javascript
> import React from 'react'
> ```
>
> jsp에서도 ES6부터 import 문법을 쓸 수 있게 되었다.
>
> 그러나 웹브라우저가 이를 이해하기에는 너무 힘들다
> `(어떤의미인지 잘 모르겠음. 첨언 필요.)`
>
> 그래서 WebPack이 필요.
>
> Webpack은 XML babel-loder를 이용해서
>
> - 린팅
> - 트랜스파일링
> - 번들링
> - 압축화
> - 난독화
>
> 의 과정을 실행해준다.



## 특징

- JSX문법으로 짠다. 그 후 XML babel-loader가 javascript로 변환해준다.

  

### 몇가지 규칙

- virtual DOM에서는 반드시 트리구조가 되어야 한다.

  - 이를 해결하기 위해 Fragment 태그가 존재(병렬로 나열가능)

- JSX에서는 자바스크립트 표현식을 사용할 수 있다.

  - 중괄호 활용하여 변수 사용가능

    ```javascript
    {name}  //처럼.
    ```

- 조건부 연산자 : 삼항연산자 사용가능, if문은 불가능

- 인라인 스타일 : 스타일 정보는 자바스크립트 객체 형식으로 만들어서 적용함. 스타일의 키 값은 카멜문법으로 작성한다.

- js에 class가 있기 때문에 중복을 피하기 위해 virtual DOM에 class명을 줄때 className을 활용해야한다.

- JSX에서는 무조건 태그를 닫아줘야한다.

  ```html
  <br> /* 처럼 사용가능했었는데 */
  ```

  ```html
  <br/> /* 처럼 무조건 닫아줘야만 함.*/
  ```

- 주석은 `//`
