import sys
sys.stdin = open('04_node.txt')

def node():
    global G
    q = [['',S,0]]
    while q:
        s = q.pop(0)
        i = 0
        while i <= len(edge)-1:
            if s[1] == edge[i][0]:
                if edge[i][1] == G:
                    return s[2]+1
                q += [edge.pop(i) + [s[2]+1]]
            elif s[1] == edge[i][1]:
                if edge[i][0] == G:
                    return s[2]+1
                q += [edge.pop(i)[::-1] + [s[2]+1]]
            else:
                i += 1
    return 0

for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    print(f'#{tc}', node())