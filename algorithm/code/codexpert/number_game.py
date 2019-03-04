n = int(input())
match = [list(map(int, input().split())) for _ in range(n)]
match = [[match[i][j] for i in range(n)] for j in range(3)]
score = [0 for _ in range(n)]

for i in range(3):
    for j in range(n):
        if match[i][j] not in match[i][:j]+match[i][j+1:]:
            score[j] += match[i][j]
for i in range(n):
    print(score[i])