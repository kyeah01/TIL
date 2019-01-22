import sys
sys.stdin = open("special_sort_input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    result = [0]*10
    minN = maxN = 0
    for i in range(10):
        if i % 2:
            for x in range(i,len(A)):
                if A[minN] > A[x]:
                    minN = x
            A[i], A[minN] = A[minN], A[i]
            minN = 0
        else:
            for y in range(i, len(A)):
                if A[maxN] < A[y]:
                    maxN = y
            A[i], A[maxN] = A[maxN], A[i]
            maxN = len(A)-1
    print(f'#{tc+1}',*A[:10])