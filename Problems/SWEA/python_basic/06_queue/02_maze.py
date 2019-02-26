import sys
sys.stdin = open('02_maze.txt')

def search(target):
    global n
    for i in range(n):
        for j in range(n):
            if maze[i][j] == target:
                return i,j

def wall(x, y):
    global n
    return True if 0 <= int(x) < n and 0 <= int(y) < n else False

def can(cnt, x,y):
    result = []
    for p in range(4):
        if wall(x+d[p],y+d[::-1][p]):
            if maze[x+d[p]][y+d[::-1][p]] == 0 or maze[x+d[p]][y+d[::-1][p]] == 3:
                result += [[cnt, x+d[p],y+d[::-1][p]]]
    return result

for tc in range(1, int(input())+1):
    d = [0,0,1,-1]
    n = int(input())
    maze = [list(map(int,input())) for _ in range(n)]
    x, y = search(2)
    e1, e2 = search(3)
    q = [[0,x,y]]
    a = [0,x,y]
    while (a[1], a[2]) != (e1, e2):
        a = q.pop(0)
        maze[a[1]][a[2]] = 1
        q += can(a[0]+1, a[1], a[2])
        if not q and (a[1], a[2]) != (e1, e2):
            print(f'#{tc}', 0)
            break
    if (a[1], a[2]) == (e1, e2):
        print(f'#{tc}', a[0]-1)