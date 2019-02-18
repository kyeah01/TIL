import sys

sys.stdin = open('02_maze_input.txt')

# 출발지점 2가 어디에 있는지 찾는 함수.
def search(matrix):
    for n in range(len(matrix)):
        try:
            print(n, matrix[n].index('2'))
            return n, matrix[n].index('2')
        except ValueError:
            continue

def back_tracking(n,m):
    global matrix
    l = len(matrix)-1
    if matrix[n-1][m] == 2:
        return 1
    elif matrix[n+1][m] == 2:
        return 1
    elif matrix[n][m-1] == 2:
        return 1
    elif matrix[n][m+1] == 2:
        return 1

    if matrix[n-1][m] == 0:
        matrix[n][m] = 4
        return back_tracking(n-1, m)
    elif matrix[n+1][m] == 0:
        matrix[n][m] = 4
        return back_tracking(n+1, m)
    elif matrix[n][m-1] == 0:
        matrix[n][m] = 4
        return back_tracking(n, m-1)
    elif matrix[n][m+1] == 0:
        matrix[n][m] = 4
        return back_tracking(n, m+1)
    else:
        return 0



for tc in range(1, int(input())+1):
    # 미로 행렬 인풋받기
    N = int(input())
    matrix = [input() for _ in range(N)]
    print(matrix)
    # 전지역에서 검색해서 2를 일단 찾아야 함.
    ans = search(matrix)
    print(ans)
    print(back_tracking(ans[0], ans[1]))