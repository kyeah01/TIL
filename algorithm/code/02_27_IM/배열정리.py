Y, X = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(Y)]


for i in range(Y):
    cnt = 1
    for j in range(X):
        if matrix[i][j] == 0:
            cnt = 1
        else:
            matrix[i][j] = cnt
            cnt += 1
    print(*matrix[i])