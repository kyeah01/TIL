import sys
sys.stdin = open('01_turn.txt')

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    L = input().split()
    print(f'#{tc}',L[M%N])