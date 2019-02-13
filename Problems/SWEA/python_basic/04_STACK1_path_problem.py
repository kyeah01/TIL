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
    L = [input().split() for i in range(E)]
    s, e = map(str, input().split())
    Route(s)
    print(f'#{tc}', result)