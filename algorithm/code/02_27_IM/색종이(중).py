matrix = [[0 for _ in range(100)] for _ in range(100)]
for tc in range(1, int(input())+1):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            matrix[x+i][y+j] = 1

cnt = 0
for i in range(100):
    if matrix[i][0] == 1 or matrix[i][99] == 1:
        cnt += 1
    if matrix[0][i] == 1 or matrix[99][i] == 1:
        cnt += 1
    for j in range(99):
        if matrix[i][j] != matrix[i][j+1]:
            cnt += 1
        if matrix[j][i] != matrix[j+1][i]:
            cnt += 1
print(cnt)