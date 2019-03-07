K = int(input())
N = int(input())

Quiz = [input().split() for _ in range(N)]
time = 210
while Quiz and time:
    person = Quiz.pop(0)
    time -= int(person[0])
    if time <0:
        break
    if person[1] == 'T':
        K += 1 if K < 8 else -7
print(K)