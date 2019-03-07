# input = 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
V = 13
E = 12
edge = list(map(int, input().split()))
edge = [edge[i:i+2] for i in range(len(edge)) if not i%2]
# left, right, root
graph = [[i,0,0,0] for i in range(1,V+1)]

for j in range(E):
    for i in range(V):
        if edge[j][0] == graph[i][0]:
            if graph[i][1]:
                graph[i][2] = edge[j][1]
            else:
                graph[i][1] = edge[j][1]
        if edge[j][1] == graph[i][0]:
            graph[i][3] = edge[j][0]

for i in range(V):
    print('{:3} {:3} {:3} {:3}'.format(graph[i][0], graph[i][1], graph[i][2], graph[i][3]))
#
# for i in range(E):
#
