import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    input()
    M = [list(map(int, input().split())) for _ in range(100)]
    cnt = 0
    for i in range(100):
        for j in range(100):
            if M[i][j] == 1:
                k = i+1
                while k < 100:
                    if M[k][j] == 1:
                        break
                    elif M[k][j] == 2:
                        cnt += 1
                        break
                    k += 1
                M[i][j] = 5
    print(f'#{tc}', cnt)