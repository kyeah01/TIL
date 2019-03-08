N = int(input())
numbers = [float(input()) for _ in range(N)]

# # prunning
# maxN = 0
# for i in range(N-1, -1, -1):
#     if numbers[i] >= 1:
#         mul, j = 1, i
#         while j > -1:
#             if not numbers[j]:
#                 break
#             mul *= numbers[j]
#             j -= 1
#             if maxN < mul:
#                 maxN = mul
# if maxN == 0:
#     maxN = max(numbers)

# Dynamic Programming
values = [1 if i else numbers[0] for i in range(N)]
i = 1
maxN = values[0]
while i < N:
    values[i] = max(numbers[i], values[i-1]*numbers[i])
    if maxN < values[i]:
        maxN = values[i]
    i += 1

print(format(maxN, '.3f'))