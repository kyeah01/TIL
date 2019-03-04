## Snail

### 문제내용

- 정사각형의 크기를 입력 받은 후 시계방향으로 돌면서 숫자를 출력하는 프로그램 만들기.

<img width="200" alt="pimg1735_1" src="https://user-images.githubusercontent.com/45934061/53693877-efb80680-3de9-11e9-81ae-9b4c37c1d180.png">



### 주의할 점

- 오른쪽, 아래, 왼쪽, 위의 순서를 지켜야 하며, 끝을 만나거나 값이 있는 곳을 만나도 다음 순서로 넘어가 넣어줘야 한다.



### 풀이방법

- 진짜로 greedy하게 풀었다!
- 오른쪽인지 왼쪽인지 아래인지 위인지 판별하면서 가야할 방향을 지정해주고, 가야하는 곳이 인덱스 밖이거나 이미 데이터가 존재하는 경우 다음 방향으로 방향을 수정하며 while문을 돌게 했다.
- 그 뒤에 출력!



#### 코드

```python
n = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]
num = 1
i,j = 0,-1
dummy = ['rignt', 'down', 'left', 'up']
direction = 0

while num <= n**2:
    if dummy[direction] == 'right':
        if j+1 == n or matrix[i][j+1]:
            direction += 1
        else:
            j += 1
            matrix[i][j] = num
            num += 1
    elif dummy[direction] == 'down':
        if i+1 == n or matrix[i+1][j]:
            direction += 1
        else:
            i += 1
            matrix[i][j] = num
            num += 1
    elif dummy[direction] == 'left':
        if j == 0 or matrix[i][j-1]:
            direction += 1
        else:
            j -= 1
            matrix[i][j] = num
            num += 1
    else:
        if i == 0 or matrix[i-1][j]:
            direction = 0
        else:
            i -= 1
            matrix[i][j] = num
            num += 1

for i in range(n):
    print(*matrix[i])
```

