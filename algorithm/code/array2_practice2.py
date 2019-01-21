# arr = [1,2,3]
# n = len(arr)

# for i in range(1<<n):
#     for j in range(n):
#         if i & (1 << j):
#             print(arr[j], end=',')
#     print()

arr = [-7, -3, -2, 5, 8]

n = len(arr)
for i in range(1, 1<<n):
    sumN = 0
    for j in range(n):
        if i & (1 << j):
            sumN += arr[j]
    if sumN == 0:
        for j in range(len(arr)):
            if i & (1 << j):
                print(arr[j], end=" ")
        print()