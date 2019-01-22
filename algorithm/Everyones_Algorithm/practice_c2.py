def find_max(Lists):
    max_number = 0
    for i in Lists:
        if max_number < i:
            max_number = i
    return max_number

def find_max_index(Lists):
    maxN = 0
    for i in range(len(Lists)):
        if Lists[maxN] < Lists[i]:
            maxN = i
    return maxN

print(find_max_index([1,5,3,6,8,2,1]))