n = int(input())
pillar = [list(map(int, input().split())) for _ in range(n)]
pillar.sort()
pillar_exist = [pillar[i][0] for i in range(n)]
maxN = 0

for i in range(n):
    if pillar[i][1] > pillar[maxN][1]:
        maxN = i

height = [0 for i in range(pillar[-1][0]+1)]
roof = 0
for i in range(pillar[maxN][0]+1):
    if i in pillar_exist:
        roof = max(roof, pillar[pillar_exist.index(i)][1])
    height[i] = roof

roof = 0
for i in range(len(height)-1, pillar[maxN][0], -1):
    if i in pillar_exist:
        roof = max(roof, pillar[pillar_exist.index(i)][1])
    height[i] = roof

print(sum(height))