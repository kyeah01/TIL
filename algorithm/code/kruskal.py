T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    edges = [list(map(int,input().split())) for _ in range(E)]
    edges.sort(key=lambda x:x[2])










def findset(x):
    if x ==p[x]:
        return x
    else:
        return findset(p[x])
    
def mst():
    global V
    c,s,i = 0,0,0
    while c < V:
        p1 = findset(edges[i][0])
        p2 = findset(edges[i][1])
        if p1 != p2:                # 사이클이 생성되지 않으면
            s += edges[i][2]        # mst에 포함되므로 가중치 추가
            c += 1                  # 간선 개수 증가
            p[p2] = p1              # 저장된 다음 간선으로 이동
        i += 1
    return s