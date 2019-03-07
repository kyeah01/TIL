student = int(input())
numbers = list(map(int, input().split()))
line = []

for stand in range(1, student+1):
    num = numbers.pop(0)
    if num:
        line = line[:-num] + [stand] + line[-num:]
    else:
        line += [stand]

print(*line)