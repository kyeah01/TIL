import sys

N, M, = map(int, sys.stdin.readline().split())
arr = list(range(N))
i = M
result = []

while arr:
    print(i)
    if i < len(arr):
        result += [arr.pop(i)]
    else:
        result += [arr.pop(i%len(arr))]
    i += M

print(result)