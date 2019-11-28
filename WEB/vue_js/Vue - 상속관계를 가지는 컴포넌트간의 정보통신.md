# Vue

## 상속관계를 가지는 컴포넌트간의 정보통신

### 자식 부모간의 데이터 공유

- 이벤트 버스를 활용하지 않는 `$emit`방식

  - 주고받는 parameter가 존재하지 않을 때

    - 부모
  
      ```html
      <div v-on:functionA="functionB"></div>
      ```

      ```javascript
      methods:{
      	functionB:{
              실행하고싶은 명령
          }   
      }
      ```
  
    - 자식

      ```html
      <div v-on:click="functionC"></div>
      ```

      ```javascript
      methods: {
          functionC: {
              this.$emit('functionA')
          }
      }
      ```
    
  - 주고받는 parameter가 존재할 때
  
    - 부모
  
      ```html
      <div v-on:functionA="functionB"></div>
      ```

      ```javascript
      methods:{
      	functionB: function (paramA, paramB) {
              실행하고싶은 명령
          }   
      }
      ```
  
    - 자식

      ```html
      <div v-on:click="functionC"></div>
      ```

      ```javascript
      methods: {
          functionC: {
              this.$emit('functionA', paramA, paramB)
          }
      }
      ```
    
