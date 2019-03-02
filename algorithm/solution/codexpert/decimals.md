## 에라토스테네스의 체

### 문제설명

- 두개의 자연수 a, b가 주어질 때, min(a,b) <= k <= max(a,b) 인 소수인 k의 개수와 min(k), max(k)의 합을 구하여라.
- 입력 값은 1<= a,b <= 100,000으로 주어진다.



### 주의할 점

- 입력값이 100,000을 가지므로 n!으로는 풀 수 없다.



### 풀이방법

- 소수를 구하는 방법에는 몇가지가 있다.
  - 최대값인 n까지 소수인지 아닌지 각각을 나누어보며 검사하는 방법.
    (이 경우 시간복잡도는 n!을 가진다.)
  - 2부터 n의 1/2까지 탐색하며 배수들을 제하는 방법.
    (n이 가장 작은 소수와의 곱으로 나타내지는 경우)
  - 위와 같이 배수들을 제하는 방법으로 사용하는데, n이 a와 b의 곱이라고 하면, a와 b 중 적어도 하나는 n<sup>1/2</sup>이하를 가지므로, 최대  n<sup>1/2</sup>까지만 배수를 제해주면 된다. : 에라토스테네스의 체
    (이 경우 시간복잡도는 nlogn을 가진다.)
- 앞 두가지 방법으로는 100,000가지의 입력값을 처리할 수 없다. 따라서 에라토스테네스의 체를 가지고 구현해야 한다.
- 소수를 2부터 max(a,b)까지 구한다음, min(a,b)와 max(a,b)사이에 있는 소수의 갯수와 가장 큰 소수, 가장 작은 소수의 합을 구한다.



##### 코드

```python
def decimals(b, t):
    check = [True]*t
    total, count, last = 0,0,0
    for i in range(2, t):
        if i <= int(t**0.5):
            if check[i]:
                for j in range(i+i, t, i):
                    check[j] = False
        if i >= b:
            if check[i]:
                count += 1
                last = i
                if count == 1:
                    total += i
    total += last
    return total, count

nums = list(map(int, input().split()))
b,t = min(nums), max(nums)
total, count = decimals(b,t)
print(count)
print(total)
```

