import sys
sys.stdin = open('04_min_sum.txt')

def sumit(N):
    global minsum
    donot = set()
    i = 0
    sumN = 0
    while len(donot) != N: 
        for j in range(N):
            if j not in donot:
                sumN += A[i][j]
                donot.update(j)
            if sumN > minsum:
                break
        else:
            minsum = sumN
        i = 0 if i == N-1 else i+1
    

for tc in range(1, int(input())+1):
    N = int(input())
    A = [list(map(int,input().split())) for i in range(N)]
    minsum = 0
    print()