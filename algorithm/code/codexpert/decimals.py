def decimals(b, t):
    check = [True]*t
    f_count, b_count, total = 0,0,0
    for i in range(2, int(t**0.5)+1):
        if check[i]:
            for j in range(i+i, t, i):
                check[j] = False
            if i >= b:
                f_count += 1
                if f_count == 1:
                    total += i
    for k in range(t-1, int(t**0.5), -1):
        if check[k]:
            b_count += 1
            if b_count == 1:
                total += k
    return total, f_count+b_count

nums = list(map(int, input().split()))
b,t = min(nums), max(nums)
total, count = decimals(b,t)
print(count)
print(total)