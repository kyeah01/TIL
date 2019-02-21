import sys
sys.stdin = open("03_tournament.txt", "r")

def half(L):
    if len(L) == 1:
        return L
    elif len(L) == 2:
        return [game(L)]
    else:
        if len(L)%2:
            return half(half(L[:len(L)//2+1]) + half(L[len(L)//2+1:]))
        else:
            return half(half(L[:len(L)//2]) + half(L[len(L)//2:]))

def game(L):
    if min(L[0][1], L[1][1]) == 1 and max(L[0][1], L[1][1]) == 3:
        return L[0] if L[0][1] < L[1][1] else L[1]
    else:
        return L[1] if L[0][1] < L[1][1] else L[0]

for tc in range(1, int(input())+ 1):
    n = int(input())
    L = list(map(int, input().split()))
    L = [[i+1,L[i]] for i in range(len(L))]
    print(f'#{tc}', half(L)[0][0])