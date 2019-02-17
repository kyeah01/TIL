def Route(s):
    global L, result, e
    if s == e:
        result = 1
        return
    for i in range(len(L)):
        if L[i][0] == s:
            z = L[i]
            L[i] = 'a'
            Route(z[1])

T = int(input())

for tc in range(1, 9):
    # 노드의 개수, 주어질 경로의 개수 인풋
    V, E = map(int, input().split())
    result = 0
    # 간선정보를 2차원 리스트로 저장받음
    # 1번 노드에서 2번 노드로 가는 경우 ['1', '2']로 저장.
    L = [input().split() for i in range(E)]
    s, e = map(str, input().split())
    # route실행하여 
    Route(s)
    print(f'#{tc}', result)