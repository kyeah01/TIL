import sys
sys.stdin = open('03_pizza.txt')

for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    pizza = [[i,v] for i, v in enumerate(cheese)]
    i = 0
    q = [pizza.pop(0) for _ in range(N)]
    while q:
        a = q.pop(0)
        if a[1] != 0:
            if a[1]//2:
                q += [[a[0], a[1]//2]]
            else:
                if pizza:
                    q += [pizza.pop(0)]
        else:
            if pizza:
                q += [pizza.pop(0)]
    print(f'#{tc}', a[0]+1)