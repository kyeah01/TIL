n = int(input())
map1 = [list(map(int, input())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if map1[i][j] == 2:
            ans = (i,j)
            break

maxN = 0
for i in range(n):
    for j in range(n):
        if map1[i][j] == 1:
            maxN = max(maxN, ((i-ans[0])**2+(j-ans[1])**2)**0.5)

print(int(maxN)) if int(maxN) >= maxN else print(int(maxN)+1)