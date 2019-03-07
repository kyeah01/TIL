n = int(input())
numbers = list(map(int, input().split()))
board = [[0 for _ in range(n*2-1)] for _ in range(n*2-1)]
start = n-1
now = start
num = 0
k = 0
Flag = True
for i in range(n*2-1):
    k = k-1 if i >= n else i+1
    for _ in range(k):
        # print(num, i, now)
        board[i][now] = numbers[num]
        num += 1
        now += 2
    if num == n*(n+1)//2:
        Flag = False
    now = abs(start-i-1)
result = 0
for i in range(n*2-1):
    sumN = 0
    for j in range(n*2-1):
        sumN += board[j][i]
    result = max(sumN, result)
print(result)