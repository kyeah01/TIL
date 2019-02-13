T = int(input())
for i in range(T):
    N, M = list(map(int, input().split()))
    A = list(map(int,input().split()))
    maxN = 0
    minN = sum(A)
    for x in range(N-M+1):
        hap = sum(A[x:x+M])
        if maxN < hap:
            maxN = hap
        if minN > hap:
            minN = hap
    print(f'#{i+1} {maxN-minN}')