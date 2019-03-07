def decimals(b, t):
    check = [True]*t
    total, count, last = 0,0,0
    for i in range(2, t):
        if i <= int(t**0.5):
            if check[i]:
                for j in range(i+i, t, i):
                    check[j] = False
        if i >= b:
            if check[i]:
                count += 1
                last = i
                if count == 1:
                    total += i
    total += last
    return total, count

nums = list(map(int, input().split()))
b,t = min(nums), max(nums)
total, count = decimals(b,t)
print(count)
print(total)