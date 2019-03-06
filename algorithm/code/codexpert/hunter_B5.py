n = int(input())
map1 = [[int(i) for i in input()] for _ in range(n)]

way = {0:[-1,-1], 1:[-1,0], 2:[-1,1], 3:[0,1], 4:[1,1], 5:[1,0], 6:[1,-1], 7:[0,-1]}
count = 0
for i in range(n):
    for j in range(n):
        if map1[i][j] == 1:
            for k in range(8):
                x,y = i,j
                while True:
                    x += way[k][0]
                    y += way[k][1]
                    if x<0 or x>=n or y<0 or y>=n:
                        break
                    elif map1[x][y] == 2:
                        map1[x][y] = 4
                        count += 1
                    elif map1[x][y] == 4:
                        continue
                    else:
                        break
print(count)