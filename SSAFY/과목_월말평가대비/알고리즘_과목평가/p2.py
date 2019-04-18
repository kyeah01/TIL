import sys

def height(sea_map, n):
    maxN = 0
    for i in range(n):
        for j in range(n):
            if maxN < sea_map[i][j]:
                maxN = sea_map[i][j]
    return maxN

sys.stdin = open('input2.txt')
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    sea_map = [list(map(int, input().split())) for _ in range(n)]
    high = height(sea_map, n)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if sea_map[i][j]:
                cnt += 1
                x = i
                while x < n:
                    y = j
                    while y < n:
                        if 0<= y-1 <n and sea_map[x][y-1]:
                            y -= 1
                        elif 0<=x<n and 0<=y<n and sea_map[x][y]:
                            sea_map[x][y] = 0
                            y += 1
                        else:
                            break
                    x += 1
                    if not 0<=x<n or not 0<=y<n:
                        break
                    elif not sea_map[x][j] and not 0<=x-2<n:
                        break
                    elif not sea_map[x][j] and not sea_map[x-2][j]:
                        break
    print('#{}'.format(tc), cnt, high)