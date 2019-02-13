def find_same(Lists):
    same = set()
    for i in range(len(Lists)):
        for j in range(i+1, len(Lists)):
            if Lists[i] == Lists[j]:
                same.add(Lists[i])
    return same

T = int(input())
for tc in range(T):
    N = int(input())
    Lists = list(map(int, input().split()))
    result = []
    start = 0
    for i in range(len(Lists)):
        if Lists[i] not in find_same(Lists) and i % 2 == 0:
            start = i
            result += Lists[i:i+2]
    for x in range(1, N):
        for y in range(N):
            if result[-1] == Lists[y*2]:
                result += Lists[y*2:(y*2)+2]
    print(f'{tc+1}', *result)

