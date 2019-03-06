def finded(board):
    here = {i:[] for i in range(6,11)}
    for i in range(n):
        for j in range(n):
            if 6 <= board[i][j] <= 10:
                here[board[i][j]] += [[i, j]]
    return here

def way(i, j, indicated):
    global n
    x,y = 1000,1000
    count = 0
    while (x,y) != (i,j):
        x,y = i,j
        n_x, n_y = direction[indicated]
        if x+n_x == i and y+n_y == j:
            return count
        elif x+n_x<0 or x+n_x>n or y+n_y<0 or y+n_y>n:
            indicated = turn[5][indicated]
            count += 1
        elif 1 <= board[x+n_x][y+n_y] <= 5:
            indicated = turn[board[x+n_x][y+n_y]][indicated]
            count += 1
        elif board[x+n_x][y+n_y] == -1:
            return count
        elif 6 <= board[x+n_x][y+n_y] <= 10:
            if [n_x, n_y] == here[board[x+n_x][y+n_y]][0]:
                x,y = here[board[x+n_x][y+n_y]][1]
            else:
                x,y = here[board[x+n_x][y+n_y]][0]
        elif board[x+n_x][y+n_y] == 0:
            x += n_x
            y += n_y
    return count


turn = {1 :{'r':'l', 'u':'d', 'd':'r', 'l':'u'}, 2 :{'r':'l', 'u':'r', 'd':'u', 'l':'d'}, 3 :{'r':'d', 'u':'l', 'd':'u', 'l':'r'}, 4 :{'r':'u', 'u':'d', 'd':'l', 'l':'r'}, 5 :{'r':'l', 'u':'d', 'd':'u', 'l':'r'}}
for tc in range(1, int(input())+1):
    n = int(input())
    board = [[int(i) for i in input().split()] for _ in range(n)]
    direction = {'r':[0,-1], 'u':[-1,0], 'd':[1,0], 'l':[0,1]}
    scores = []
    here = finded(board)
    for i in range(n):
        for j in range(n):
            if not board[i][j]:
                for k in direction:
                    scores += [way(i, j, k)]
    print(f'#{tc}',max(scores))