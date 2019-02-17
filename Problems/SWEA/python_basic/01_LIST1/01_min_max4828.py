T = int(input())
for x in range(T):
    maxN = 0
    N = int(input())
    A = list(map(int,input().split()))
    minN = A[0]
    for i in range(len(A)):
        if A[i] > maxN:
            maxN = A[i]
        if A[i] < minN:
            minN = A[i]
    print(maxN, minN) 
    ans = maxN - minN
    print(f'#{x+1} {ans}')