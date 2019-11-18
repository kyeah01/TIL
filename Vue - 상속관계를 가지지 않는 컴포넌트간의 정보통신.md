# Vue

## 상속관계를 가지지 않는 컴포넌트간의 통신

### Event Bus를 활용한 데이터 공유

- Event Bus Define

  - 스크립트 내에서 정의

    ```javascript
    const EventBus = new Vue();
    ```

  - 외부 컴포넌트로 활용

    ```javascript
    import Vue from 'vue'
    const EventBus = new Vue();
    export default EventBus;
    ```

- 이벤트 발행

  ```javascript
  EventBus.$emit('functionA', argumentA)
  ```

- 이벤트 수신

  ```javascript
  EventBus.$on('functionA', functionB)
  ```

  ```javascript
  functionB (argumentA) {
      console.log(argumentA)
  }
  ```

  