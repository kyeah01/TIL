연속한 부분의 최대 곱 구하기

### 문제 내용

- n개의 양의 실수가 있을 때, 한 개 이상의 연속된 수들의 곱이 최대가 되는 부분을 찾아 그 곱을 출력하는 프로그램. n은 10,000이하의 자연수.
- 만약 다음과 같이 8개의 양의 실수가 주어지면,
  ![1](https://user-images.githubusercontent.com/45934061/53683416-eecc9980-3d43-11e9-99bc-74567ab8e0f5.gif)
  회색으로 칠해진 1.3, 0.9, 1.4를 곱한 값 1.638이 최대가 된다.



### 주의할 점

- n의 크기가 최대 10,000을 가지므로 완전검색으로는 풀 수 없다.
- 가지치기를 하거나 dynamic programming을 사용해 풀어야 한다.
- 소수점 세번째 자리까지 프린트해야 하는데, 소수점 세자리보다 짧게 나올 수 있으므로 (1처럼) round로는 풀 수 없다.



### 풀이방법

#### Prunning

<img width="500" alt="2" src="https://user-images.githubusercontent.com/45934061/53683392-9ac1b500-3d43-11e9-98ce-1b9ee03b1715.png">

- 완전 검색을 사용할시, 0부터 n까지 각각의 위치에서 출발해서, 리스트의 끝까지 곱을 구하면서 최대값을 갱신해가는 방식을 활용할 수 있다. 이 경우, 연산 크기는 n!를 가진다.
- 연산 크기를 줄이기위해 몇가지 방법의 가지치기가 가능하다.
  - 1보다 작으면 곱했을때에 오히려 값이 더 작아지므로, 각각의 값이 1을 넘지 않는 경우에 구간합을 구하기 위해 출발하지 않게 가지치기한다.
    (1보다 큰 경우에만 출발해서 부분 곱을 구한다는 말이 좀 더 맞을 수도 있을 것 같다.)
    - 이 경우, 리스트의 모든 값이 1보다 작은 경우에는 모든 구간에서 구간곱을 구하지 않기때문에 가장 큰 구간곱을 구하기 위해 할당했던 maxN값이 초기값을 그대로 가지므로 마지막에 maxN이 초기값일 경우 리스트의 가장 큰 값을 가지게 할당해준다.
  - 또 하나는 중간에 0이 끼여있는 경우이다. 0이 나오면 모든값이 초기화되므로 루프를 나가게 가지치기 해준다.

##### 코드

```python
N = int(input())
numbers = [float(input()) for _ in range(N)]

maxN = 0
for i in range(N-1, -1, -1):
    if numbers[i] >= 1:
        mul, j = 1, i
        while j > -1:
            if not numbers[j]:
                break
            mul *= numbers[j]
            j -= 1
            if maxN < mul:
                maxN = mul
if maxN == 0:
    maxN = max(numbers)

print(format(maxN, '.3f'))
```



#### Dynamic Programming

- memoization을 활용해 연산크기를 줄인다.
- 처음부터 출발해서 지금까지 가져온 section의 곱을 확인하면서 현재 가지고 있는 값과 비교해서 큰 값을 취한다. 이렇게 하면 이전 섹션을 곱에 포함할 것인지 포함하지 않을 것인지 판단하는 것과 같다.
- 이경우에는 앞의 값과 비교해야 하므로 인덱스 에러가 나지 않게 주의하면서 풀이해야 한다.



##### 코드

```python
N = int(input())
numbers = [float(input()) for _ in range(N)]

values = [1 if i else numbers[0] for i in range(N)]
i = 1
maxN = values[0]
while i < N:
    values[i] = max(numbers[i], values[i-1]*numbers[i])
    if maxN < values[i]:
        maxN = values[i]
    i += 1

print(format(maxN, '.3f'))
```

