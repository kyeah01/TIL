# Stack

![01](https://user-images.githubusercontent.com/45934061/53683464-4f5bd680-3d44-11e9-8e83-7bd4b4e3ce17.png)



## Stack 개념

1. stack이란

   - 선형구조 자료. 쌓아올린 형태.
   - LIFO(후입선출)방식을 따른다.

2. Stack의 구현

   - C의 경우 배열을 활용.
   - Python의 경우 리스트를 활용한다.
     : 저장소 자체를 스택이라고 부르기도 한다.
   - stack에서 가장 마지막에 삽입된 원소의 위치를 Top이라고 한다.

3. Stack의 연산

   - 삽입(push) : 자료저장
   - 삭제(pop) : 자료를 꺼냄(LIFO방식으로 맨 위의 항목 제거)
   - isEmpty : 스택이 공백인지 아닌지 확인연산
   - peek : 스택이 top에 있는 원소를 반환하는 연산

     ![02 stack](https://user-images.githubusercontent.com/45934061/53683465-4ff46d00-3d44-11e9-9d29-d2bec39044fd.png)
   -> 언더플로우(stack이 이미 0이 되었는데도 pop을 연산하는 경우)에 대한 처리가 필요하다.


4. (Python) 리스트를 사용한 경우
   - 구현이 용이하다.
   - 리스트의 크기변경 작업이 시간을 많이 먹는다.
     해결방법?
     - 리스트의 크기가 변동되지 않도록 배열처럼 크기를 정해놓고 사용하거나
     - 동적 연결 리스트를 이용, 저장소 동적 할당 후에 스택을 구현하는 방식
       : 구현이 용이하고 시간을 절약할 수 있으나
         리스트 구현보다 구현이 복잡하다.



## Stack 응용

1. 괄호검사

   ~~~python
   T = int(input())
   
   def bracket(String):
       check = { ')' : '(' , '}' : '{' , ']' : '[' }
       h = []
       for i in range(len(String)):
           if String[i] in check.values():
               h.append(String[i])
           elif String[i] in check.keys():
               if len(h) == 0:
                   return 0
               elif h[-1] == check[String[i]]:
                   h.pop()
               else:
                   return 0
       if len(h) == 0:
           return 1
       else:
           return 0
   
   for tc in range(1, T + 1):
       S = input()
       print(f'#{tc}', bracket(S))
   ~~~

   

2. function call : 재귀함수



## Memoization

1. 피보나치 수열의 재귀함수
   : call tree 확인 시 중복호출이 계속해서 일어나는 것을 확인할 수 있다. 중복호출의 해소를 위해 **Memoization**이 필요하다.
2. Memoization
   - 의미 : 컴퓨터 프로그램 실행시 이전 계산 값을 메모리 저장하여 매번 다시 실행하는 것을 막는 것.
   - DP(동적계획법)의 핵심이 되는 기술이다.
   - 주로 arr나 Stack형식으로 활용한다.









##### Reference

SWEA python imtermediate - stack1

https://gmlwjd9405.github.io/2018/08/03/data-structure-stack.html

https://ko.wikipedia.org/wiki/%EC%96%B8%EB%8D%94%ED%94%8C%EB%A1%9C