import sys
sys.stdin = open('190129_palindrome_input.txt')

T = int(input())

for tc in range(1, T+1):
    n,m = map(int, input().split())
    lists = [input() for x in range(n)]
    if m != n:
        for x in range(n):
            for y in range(n-m+1):
                if lists[x][y] == lists[x][-n+y+m-1]:
                    for i in range(m//2):
                        if lists[x][y+i] != lists[x][-n+y+m-1-i]:
                            break
                    else:
                        print(f'#{tc}', lists[x][y:y+m])
                elif lists[y][x] == lists[-n+y+m-1][x]:
                    for i in range(m//2):
                        if lists[y+i][x] != lists[-n+y+m-1-i][x]:
                            break
                    else:
                        print(f'#{tc}', end=' ')
                        for i in range(m):
                            if i == (m-1):
                                print(lists[y+i][x])
                            else:
                                print(lists[y+i][x], end='')
    else:
        for x in range(n):
            if lists[x][0] == lists[x][-1]:
                for i in range(m//2):
                    if lists[x][i] != lists[x][-n+m-1-i]:
                        break
                else:
                    print(f'#{tc}', lists[x])
            elif lists[0][x] == lists[-1][x]:
                for j in range(m//2):
                    if lists[j][x] != lists[-j-1][x]:
                        break
                else:
                    print(f'#{tc}', end=' ')
                    for z in range(m):
                        if z == (m-1):
                            print(lists[z][x])
                        else:
                            print(lists[z][x], end='')