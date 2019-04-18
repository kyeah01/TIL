def anypang(n,k,board):
    minN = 10000000
    for i in range(n-2):
        for j in range(n-2):
            sum1, sum2 = 0, 0
            for m in range(k):
                sum1 += board[i+m][j+m]
                sum2 += board[i+k-(m+1)][j+m]
            minN = min(abs(sum1-sum2), minN)
    return minN

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    print('#{}'.format(tc), anypang(n,k, board))