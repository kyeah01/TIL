n, k = map(int, input().split())
board = [[int(inp) for inp in input().split()] for _ in range(n)]
maxN = 0
for i in range(n-k+1):
    for j in range(n-k+1):
        sumN = 0
        for t in range(k):
            sumN += sum(board[i+t][j:j+k])
            if 0<t<k-1:
                sumN -= sum(board[i+t][j+1:j+k-1])
        maxN = max(maxN, sumN)
print(maxN)