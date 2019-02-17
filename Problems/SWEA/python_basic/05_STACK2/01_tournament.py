import sys
sys.stdin = open("01_tournament.txt", "r")

def half(n,L):
    if n == 1:
        return s,e
    if n%2:
	    s = tournament(n//2+1, L[:n//2+1])
	    e = tournament(n//2, L[n//2+1:])
    else:
	    s = tournament(n//2, L[:n//2])
	    e = tournament(n//2, L[n//2:])

def tournament(n, L):
    if n == 1:
        return n, L
    for i in range(n//2):
        if (max(L[i][1], L[i+1][1]), min(L[i][1], L[i+1][1])) == (3,1):
            L.pop(i+1) if L[i][1] < L[i+1][1] else L.pop(i)
        else:
            L.pop(i) if L[i][1] < L[i+1][1] else L.pop(i+1)
    n = n //2 + 1 if n%2 else n//2
    return half(n, L)

# def tournament(n, L):
#     if n == 1:
#         return 0.5,L
#     for i in list(range(n//2)):
#         if (max(L[i][1], L[i+1][1]), min(L[i][1], L[i+1][1])) == (3,1):
#             L.pop(i+1) if L[i][1] < L[i+1][1] else L.pop(i)
#         else:
#             L.pop(i) if L[i][1] < L[i+1][1] else L.pop(i+1)
#     return n,L

for tc in range(1, int(input())+ 1):
    n = int(input())
    L = list(map(int, input().split()))
    L = [[i+1,L[i]] for i in range(len(L))]
    print(half(n,L))
    

    # print(f'#{tc}')