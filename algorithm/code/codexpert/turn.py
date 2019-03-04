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