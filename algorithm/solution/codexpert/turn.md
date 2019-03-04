## 회전

### 문제 설명

- 정사각형의 크기와 정사각형에 들어갈 숫자를 입력받은 후, 시계방향으로 회전하는 프로그램 작성하기.

  

  <img width="600" alt="pimg1735_1" src="https://user-images.githubusercontent.com/45934061/53693040-68649600-3ddd-11e9-9c40-edd9bd9d0f5e.png">

- 회전의 크기가 0이 주어지면 종료된다.

### 주의할 점

- 0, 90, 180, 270, 360이 아닌 각도를 입력받으면 출력하지 않고 다시 입력받아야 한다.

- 처음에 입력 받은 매트릭스가 계속 유지되는 것이 아니라 2차 이상의 수행때는 전의 회전된 매트릭스를 가지고 회전시켜야 한다.

### 풀이방법

- 90도 회전을 2번 시키면 180도, 3번 시키면 270도. 따라서 90도 회전을 구현한 다음 반복하도록 풀이했다.

- 90도 회전시키면 첫번째 열이 첫번째 행이 되는 것과 같다.

#### 코드

```python
n = int(input())
matrix = [input().split() for _ in range(n)]

while True:
    angle = int(input())
    if angle == 0:
        break
    elif angle in [90, 180, 270]:
        for _ in range(angle//90):
            matrix = [[matrix[i][j] for i in range(n-1, -1, -1)] for j in range(n)]
        for i in range(n):
            print(*matrix[i])
    elif angle == 360:
        for i in range(n):
            print(*matrix[i])
```