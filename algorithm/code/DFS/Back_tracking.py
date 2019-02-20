# 백트래킹 기법으로 Power set 구하기
# 

graph = {'A': ['B', 'C', 'D'],
         'B': ['A', 'E', 'F'],
         'C': ['A', 'G'],
         'D': ['A', 'H', 'I'],
         'E': ['B'],
         'F': ['B', 'J'],
         'G': ['C'],
         'H': ['D'],
         'I': ['D', 'K', 'L'],
         'J': ['F'],
         'K': ['I'],
         'L': ['I']}

def DFS(graph, root):
    stack = []
    visited = []

    stack.extend(root)

    while stack:
        visited += [stack.pop()]
        #print(outputFromStack)
        inputToStack = list(set(graph[visited[-1]]) - set(visited))
        inputToStack.sort()
        stack.extend(inputToStack)

    return visited

print(DFS(graph, 'A'))

# stack, visit의 빈 리스트 선언
# 출발값을 stack에 더해준다
# while stack이 존재하는 동안
#   visit에 stack값을 pop해서 더해줌
#   visit에 방금 집어넣은 stack의 가장 마지막 값의 인접 노드들을 뽑아온다.
#   set로 바꿔서 visited의 