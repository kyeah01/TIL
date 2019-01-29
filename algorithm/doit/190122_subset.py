import sys
sys.stdin = open("subset_input.txt")

def subset(N, K):
    A = range(1,13)
    ct2 = 0
    for i in range(1<<len(A)):
        sumN = 0
        ct = 0
        for j in range(12):
            if i & (1<<j):
                sumN += A[j]
                ct += 1
        if ct == N and sumN == K:
            ct2 += 1
    return ct2

T = int(input())
for i in range(T):
	N, K = map(int, input().split())
	print(f'#{i+1}',subset(N,K))