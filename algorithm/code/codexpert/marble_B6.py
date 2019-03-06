r,c = map(int, input().split())
map1 = [[int(i) for i in input()] for _ in range(c)]
n = int(input())
indicated = list(map(int, input().split()))
direction = {1:[-1,0], 2:[1,0], 3:[0,-1], 4:[0,1]}
now = indicated.pop(0)
for i in range(r):
    for j in range(c):
        if map1[i][j] == 2:
            x,y = i,j
            map1[i][j] = 'm'
            break
while indicated or now:
    nx = x + direction[now][0]
    ny = y + direction[now][1]
    if nx < 0 or nx > c-1 or ny < 0 or ny > r-1 or map1[nx][ny]==1:
        now = indicated.pop(0) if indicated else 0
    else:
        x,y = nx, ny
        map1[x][y] = 'm'
count = 0
for m in map1:
    count += m.count('m')
print(count)