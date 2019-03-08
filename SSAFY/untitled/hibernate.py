N = int(input())
numbers = list(map(int, input().split()))

values = [0 if i else numbers[0] for i in range(N)]
idiot = values[0]
smart = 0 if numbers[0] < 0 else numbers[0]

i = 1
while i < N:
    if numbers[i] > 0:
        smart += numbers[i]
    values[i] = max(numbers[i], values[i-1]+numbers[i])
    if idiot < values[i]:
        idiot = values[i]
    i += 1
if smart == 0:
    smart = max(numbers)

print(idiot, smart)