def minheap(n):
    i = 0
    stack = []
    result = []
    while n > 2**i:
        # 만약에 자식노드가 있으면,
        if len(node[i]) > 2:
            i = node[i][2]
            stack += [node[i]]
        else:
            s = stack.pop()
            result += [s[1]]


# for tc in range(10):
n = int(input())
node = [input().split() for _ in range(n)]
minheap(n)