n = int(input())
numbers = [list(map(int, input().split())) for _ in range(n)]
match = [[numbers[i][j] for i in range(n-1, -1, -1)] for j in range(3)]
score = [0]*n

for i in range(3):
    for x in match[i]:
        times = match[i].count(x)
        if times > 1:
            for _ in range(times):
                match[i].remove(x)

for i in range(n):
    for j in range(3):
        if numbers[i][j] in match[j]:
            score[i] += numbers[i][j]
    print(score[i])