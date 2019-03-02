## 연속된 부분의 최대 합 구하기

### 문제 내용

- -10<sup>4</sup> 이상,  10<sup>4</sup> 이하인 수가 정수로 주어질 때, 이 수들의 연속된 합이 가장 최대가 되는 경우와 임의의 수를 모두 더해 최대가 되는 경우 두가지를 모두 구한다.
- 예를 들어 2, -1, 2, 3, 4, -5가 주어지면, 첫번째 경우에는 2,-1,2,3,4를 더해서 10이 되는 경우, 두번째 경우는 2,2,3,4를 더해 11이 되는 경우가 최적의 경우이다.



### 주의할 점

- n이 10<sup>5</sup>까지 주어지므로 완전검색을 통해서는 풀 수 없다.
- dynamic program을 통해 풀어야 한다.



### 풀이방법

- memoization을 활용해 연산크기를 줄인다.
- 똑똑하게 sum을 구하는 경우에는, 0보다 큰 값을 가지는 경우 모두 더해준다.
- 그렇지 않은 경우, 처음부터 출발해서 지금까지 가져온 section의 합을 확인하면서 현재 가지고 있는 값과 비교해서 큰 값을 취한다. 이렇게 하면 이전 섹션을 합에 포함할 것인지 포함하지 않을 것인지 판단하는 것과 같다.
- 이경우에는 앞의 값과 비교해야 하므로 인덱스 에러가 나지 않게 주의하면서 풀이해야 한다.



##### 코드

```python
N = int(input())
numbers = list(map(int, input().split()))

values = [0 if i else numbers[0] for i in range(N)]
idiot = values[0]
smart = 0 if numbers[0] < 0 else numbers[0]

i = 1
while i < N:
    if numbers[i] > 0:
        smart += numbers[i]
    values[i] = max(numbers[i], values[i-1]+numbers[i])
    if idiot < values[i]:
        idiot = values[i]
    i += 1
if smart == 0:
    smart = max(numbers)

print(idiot, smart)
```

