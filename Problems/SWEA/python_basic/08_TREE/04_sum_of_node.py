import sys
sys.stdin = open('4.txt')

for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    nodes = [list(map(int, input().split())) for _ in range(M)]
    tree = [0 for _ in range(N+1)]
    for node in nodes:
        tree[node[0]] = node[1]
    i = N
    while i//2:
        tree[i//2] += tree[i]
        i -= 1
    print(f'#{tc}',tree[L])