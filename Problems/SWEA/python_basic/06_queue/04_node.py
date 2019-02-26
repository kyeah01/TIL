import sys
sys.stdin = open('04_node.txt')


for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    q = [[S,'',0]]
    while q:
        s = q.pop(0)
        q += [edge[i] + [s[2]+1] for i in range(len(edge)) if edge[i][0] == s[0]]
    print(s)