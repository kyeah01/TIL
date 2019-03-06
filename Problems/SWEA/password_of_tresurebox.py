for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    knife = N//4
    numbers = list(input())
    complete = set()
    for _ in range(N-1):
        for i in range(4):
            complete.update({''.join(numbers[i*knife:(i+1)*knife])})
        numbers += [numbers.pop(0)]
    complete = list(map(lambda x:int(x,16), complete))
    complete.sort(reverse=True)
    print(f'#{tc}',complete[K-1])