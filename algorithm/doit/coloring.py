import sys
sys.stdin = open("coloring_input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    skechbook = [[set() for _ in range(10)] for _ in range(10)]
    for _ in range(N):
        r1, c1, r2, c2, C = map(int, input().split())
        if C == 1:
            for x in range(r1,r2+1):
                for y in range(c1,c2+1):
                    skechbook[x][y].add('1')
        if C == 2:
            for x in range(r1,r2+1):
                for y in range(c1,c2+1):
                    skechbook[x][y].add('2')
    cnt = 0
    for i in range(10):
        for j in range(10):
            if len(skechbook[i][j]) == 2:
                cnt += 1
    print(f'#{tc+1} {cnt}')
