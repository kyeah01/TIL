T = int(input())

for tc in range(1, T + 1):
    # 노드의 개수, 주어질 경로의 개수 인풋
    V, E = map(int, input().split())
    
    L = [input().replace(' ', '') for i in range(E)]
    L.sort()
    s, e = map(int, input().split())
    visit = [s,]


def Route(s, e):
    global visit
    global L
    if s == e:
        return 1
    else:
        while visit:
            for i in range(len(L)):
                if i not in visit and L[i][0] == s:
                    s = L[i][1]
                    visit += [i]
                    Route(s, e)
                    break
            else:
                s = visit.pop()
                Route(s, e)
                








def check(matrix, s, e):
    global visit
    if s == e:
        return 1
    elif sum(matrix[s]) == 0:
        check(matrix, visit.pop(), e)
    else:
        for i in range(len(matrix[s])):
            if matrix[s][i] and i not in visit:
                visit += [s]
                check(matrix, i, e)

T = int(input())

for tc in range(1, T + 1):
    # 노드의 개수, 주어질 경로의 개수 인풋
    V, E = map(int, input().split())
    
    # 빈행렬 만들기
    matrix = [[0 for _ in range(V)] for _ in range(V)]
    
    # matrix 행렬을 경로행렬로 가공하기.
    # 이 경우 노드 1은 노드0으로, 노드 2는 노드 1로 간주된다.
    # 단방향 통행이 가능한 경우이기 때문에 다음과 같이 가공한다.
    for _ in range(E):
        # 경로 인풋 받기
        s, e = map(int, input().split())
        # 경로 있으면 1로 바꿔주기
        matrix[s-1][e-1] = 1
    # 출발지점과 도착지점을 인풋받는다.
    s, e = map(int, input().split())
    visit = []
    print(check(matrix, s, e))





for tc in range(10):
    V, E = map(int, input().split())


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

for tc in range(1, T + 1):
    # 노드의 개수, 주어질 경로의 개수 인풋
    V, E = map(int, input().split())
    result = 0
    L = [input().replace(' ', '') for i in range(E)]
    s, e = map(str, input().split())
    Route(s)
    print(f'#{tc}', result)