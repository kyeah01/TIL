def check(total, nomi, num):
    number = [0,0,0]
    for j in range(n):
        for i in nomi:
            if vote[j][i] == num:
                number[i] += 1
    maxN = max(number)
    nomi = [i for i in range(3) if maxN == number[i]]
    if len(nomi) == 1:
        return (nomi[0]+1, total)
    elif num == 1:
        return (0, total)
    else:
        return check(total, nomi, num-1)

n = int(input())
vote = [list(map(int, input().split())) for _ in range(n)]

total = [0,0,0]
for i in range(n):
    for j in range(3):
        total[j] += vote[i][j]
maxN = max(total)

nomi = [i for i in range(3) if maxN == total[i]]
if len(nomi) == 1:
    print(nomi[0]+1, maxN)
else:
    print(*check(maxN, nomi, 3))