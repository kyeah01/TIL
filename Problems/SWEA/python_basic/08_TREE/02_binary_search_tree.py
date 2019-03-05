import sys
sys.stdin = open('2.txt')

def inorder(n):
    global result
    if n != 0:
        inorder(arr[n][0])
        result += [n]
        inorder(arr[n][1])

for tc in range(1, 1+int(input())):
    n = int(input())
    L = list(range(n+1))
    result = []
    make = list(range(2, n+1))
    arr = [[0, 0] for _ in range(n+1)]
    for i in range(1, n+1):
        arr[i][0] = make.pop(0)
        if not make:
            break
        arr[i][1] = make.pop(0)
        if not make:
            break

    inorder(1)
    answer = [0 for _ in range(n)]
    a = 1
    for i in result:
        answer[i-1] = a
        a += 1
    print(answer)
    # print(f'#{tc}', answer[0], answer[n//2])
    