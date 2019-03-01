N = int(input())
numbers = [float(input()) for _ in range(N)]

def recur(mul, i):
    global maxN
    if maxN < mul:
        maxN = mul
    else:
        return 
    if i == N:
        return 
    return recur(mul*numbers[i], i+1)

mul = 1
maxN = 0
for i in range(N):
    if numbers[i] >= 1:
        recur(mul, i)
print(round(maxN, 3))