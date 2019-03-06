n = int(input())
maze = [[int(i) for i in input()] for _ in range(n)]
indicated = list(map(int,input().split()))
now, cnt = 0, 0
i, j = 0, 0
maze[i][j] = 'r'
direction = {1:[1, 0], 2:[0, -1], 3:[-1, 0], 4:[0, 1]}
while True:
    new_i, new_j = direction[indicated[now]]
    if i+new_i < 0 or i+new_i > n-1 or j+new_j < 0 or j+new_j>n-1 or maze[i+new_i][j+new_j]==1:
        now += 1 if now!=3 else -3
    elif maze[i+new_i][j+new_j]==0:
        i,j = i+new_i, j+new_j
        maze[i][j] = 'r'
        cnt += 1
    else:
        print(cnt)
        break