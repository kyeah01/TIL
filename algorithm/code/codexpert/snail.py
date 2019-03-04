n = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]
num = 1
i,j = 0,-1
dummy = ['rignt', 'down', 'left', 'up']
direction = 0

while num <= n**2:
    if dummy[direction] == 'right':
        if j+1 == n or matrix[i][j+1]:
            direction += 1
        else:
            j += 1
            matrix[i][j] = num
            num += 1
    elif dummy[direction] == 'down':
        if i+1 == n or matrix[i+1][j]:
            direction += 1
        else:
            i += 1
            matrix[i][j] = num
            num += 1
    elif dummy[direction] == 'left':
        if j == 0 or matrix[i][j-1]:
            direction += 1
        else:
            j -= 1
            matrix[i][j] = num
            num += 1
    else:
        if i == 0 or matrix[i-1][j]:
            direction = 0
        else:
            i -= 1
            matrix[i][j] = num
            num += 1

for i in range(n):
    print(*matrix[i])