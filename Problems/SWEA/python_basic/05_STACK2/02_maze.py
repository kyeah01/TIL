import sys

sys.stdin = open('02_maze_input.txt')

# 출발지점 2가 어디에 있는지 찾는 함수.
def search(matrix):
    for n in range(len(matrix)):
        try:
            return n, matrix[n].index(2)
        except ValueError:
            continue

def check(n,m,l):
    return True if 0 <= m <= l and 0 <= n  <= l else False

def back_tracking(n,m):
    global matrix, result,N
    l = N-1
    matrix[n][m] = 4
    if check(n-1,m,l) and matrix[n-1][m] == 3:
        result = 1
        return
    if check(n+1,m,l) and matrix[n+1][m] == 3:
        result = 1
        return
    if check(n,m-1,l) and matrix[n][m-1] == 3:
        result = 1
        return
    if check(n,m+1,l) and matrix[n][m+1] == 3:
        result = 1                                      
        return
    if check(n-1,m,l) and matrix[n-1][m] == 0:
        back_tracking(n-1, m)
    if check(n+1,m,l) and matrix[n+1][m] == 0:
        back_tracking(n+1, m)
    if check(n,m-1,l) and matrix[n][m-1] == 0:
        back_tracking(n, m-1)
    if check(n,m+1,l) and matrix[n][m+1] == 0:
        back_tracking(n, m+1)

for tc in range(1, int(input())+1):
    # 미로 행렬 인풋받기
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    # 전지역에서 검색해서 2를 일단 찾아야 함.
    ans = search(matrix)
    result = 0
    back_tracking(ans[0], ans[1])
    print(result)