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