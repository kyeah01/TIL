step, chart = input().split()
chart = list(chart)
i = 0
lenth = len(chart)

hierarchy = {i:[] for i in range(51)}
visited = []
cnt = 0
for i in range(lenth):
    if chart[i] == '<':
        cnt += 1
    elif chart[i] == '>':
        cnt -= 1
    elif i not in visited:
        k = i
        while chart[k] not in {'<', '>'}:
            k += 1
        hierarchy[cnt] += [''.join(chart[i:k])]
        visited += list(range(i, k))
print(*hierarchy[int(step)])