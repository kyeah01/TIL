def sumN1(n):
    s = 0
    for i in range(1, n+1):
        s += i
    return s

print(sumN1(10))
print(sumN1(100))

def sumN2(n):
    return n*(n+1)//2

print(sumN2(10))
print(sumN2(100))