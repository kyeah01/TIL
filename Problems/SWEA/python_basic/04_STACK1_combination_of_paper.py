T = int(input())

for tc in range(1, T + 1):
    N = int(input())/10
    L = [1,3]
    for i in range(2, N):
        L += list(L[N-1] + 2 * L[N-2])
    print(f'#{tc}', L[N-1])