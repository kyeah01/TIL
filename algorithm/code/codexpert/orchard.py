n = int(input())
field = [[int(i) for i in input()] for _ in range(n)]

cnt = 0
for i in range(1,n):
    for y in range(1,n):
        sumUL, sumUR, sumDL, sumDR = 0, 0, 0, 0
        for x in range(i):
            for k in range(n-y):
                sumUL += field[:i][x][k]
            for k in range(n-y, n):
                sumUR += field[:i][x][k]
        for x in range(n-i):
            for k in range(n-y):
                sumDL += field[i:][x][k]
            for k in range(n-y, n):
                sumDR += field[i:][x][k]
        if sumUL == sumUR == sumDL == sumDR:
            cnt += 1
print(cnt) if cnt else print(-1)