C, R = map(int, input().split())
K = int(input())

if 1 < K <= C*R: 
    i,j = 0,0
    # r, d, l, u
    direction = [[0,1],[1, 0],[0,-1],[-1,0]]
    indicated, num = 0, 1
    matrix = [[0 for _ in range(R)] for _ in range(C)]
    while num < C*R+1:
        how_i, how_j = i+direction[indicated][0], j+direction[indicated][1]
        if num == C*R:
            i = how_i
            j = how_j+1
            break
        elif how_i<0 or how_i>=C or how_j<0 or how_j>=R or matrix[how_i][how_j]:
            indicated += 1 if indicated < 3 else -3
        else:
            matrix[i][j] = num
            if num == K:
                break
            num += 1
            i = how_i
            j = how_j
    print(i+1,j+1)
elif K == 1:
    print(1,1)
else:
    print(0)