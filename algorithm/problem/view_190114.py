import sys 
sys.stdin = open('view_input.txt')
T = 10
for tc in range(T):
    ans = 0
    N = int(input())
    apt = list(map(int,input().split()))
    for i in range(2, N-2):
        if apt[i] > max(apt[i-2],apt[i-1], apt[i+1], apt[i+2]):
            ans += apt[i] - max(apt[i-2],apt[i-1], apt[i+1], apt[i+2])
    print(f'#{tc+1} {ans}')