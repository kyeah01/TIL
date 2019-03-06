## Snake

### 문제 설명

- snake게임 구현하기
- 뱀이 몸 길이를 늘려서 머리를 다음 칸으로 이동한다.
- 이동한 칸에 과일이 있으면 몸길이가 증가된 상태가 유지된다.
- 만약 과일이 없다면, 몸길이가 원상태로 돌아오게 된다. 이때, 꼬리가 위치한 칸을 비우게 된다.
- L이 주어지면 왼쪽으로 90도, D가 주어지면 오른쪽으로 90도 간다.
- 이때, 뱀이 이동한 총 거리를 출력한다.



### 주의할 점

- 주어지는 시간은 누적시간으로 주어진다.
- 방향전환 명령이 없을 시 끝까지 가다가 벽에 부딪힌 시간을 출력한다.



### 풀이방법

- 2차원 배열에 게임판을 정의하고, 과일을 위치시킨다. 그 후 뱀을 직접 이동시킨다.
- 뱀이 길어질때는 헤드를 기준으로 길어지지만, 짧아질때는 꼬리를 기준으로 짧아진다. 뱀이 놓여있는 위치를 리스트로 만들고, 짧아져야 할 때마다 꼬리를 pop시켜준다.



#### 코드

```python
def snake(board, way, n):
    # 오른쪽 위 왼쪽 아래
    direc = [[0,1], [-1, 0], [0, -1], [1, 0]]
    di, cnt, time = 0, 0, 0
    snake = [[0,0]]
    while True:
        if way:
            go = way.pop(0)
        else:
            go = (10000000,0)
        for _ in range(int(go[0])-time):
            cnt += 1
            x, y = snake[-1][0]+direc[di][0], snake[-1][1]+direc[di][1]
            snake += [[x,y]]
            if 0 > x or x >= n or 0 > y or y >= n:
                return cnt
            elif board[x][y] == 's':
                return cnt
            elif board[x][y] == 0:
                tail = snake.pop(0)
                board[tail[0]][tail[1]] = 0
            board[x][y] = 's'
        time = int(go[0])
        if go[1] == 'D':
            #  -> (0->3) (1, 0) (2,1) (3,2)
            di = 3 if not di else di-1
        else:
            #  -> (0->1) (1, 2) (2,3) (3,0)
            di = di+1 if di != 3 else 0

n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]
board[0][0] = 's'
ea = int(input())
fruit = [list(map(int, input().split())) for _ in range(ea)]
for f in fruit:
    board[f[0]-1][f[1]-1] = 'f'
times = int(input())
way = [input().split() for _ in range(times)]

print(snake(board, way, n))
```

