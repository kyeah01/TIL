def bingo(match):
    cnt = 0
    for x in match:
        if len(match[x]) == 5:
            cnt += 1
    for i in range(5):
        for j in range(5):
            if i not in match[j]:
                break
        else:
            cnt += 1
    for i in range(5):
        if i not in match[i]:
            break
    else:
        cnt += 1
    for i in range(5):
        if i not in match[4-i]:
            break
    else:
        cnt += 1
    return cnt

def check(arr, numbers):
    match = {i:[] for i in range(5)}
    for i in range(5):
        for j in range(5):
            for k in range(5):
                if numbers[i][j] in arr[k]:
                    match[k] += [arr[k].index(numbers[i][j])]
                    break
            if bingo(match) >= 3:
                return i*5+j+1

arr = [input().split() for _ in range(5)]
numbers = [input().split() for _ in range(5)]
print(check(arr, numbers))