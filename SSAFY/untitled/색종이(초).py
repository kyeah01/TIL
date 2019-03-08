# color = {list(map(int, input().split())) for tc in range(1, int(input())+1)}

# area = len(color)*100
#
# for x in color:
#     for y in color:
#         if x != y:
#             if x[0] <= y[0] <= x[0]+10:
#                 if x[1] <= y[1] <= x[1]+10:
#                     area -= (y[0] - x[0]) * (y[1] - x[1])
#                 elif x[1] <= y[1]+10 <= x[1]+10:
#                     area -= (y[0] - x[0]) * (x[1] - y[1])
# print(area)

matrix = [[0 for _ in range(100)] for _ in range(100)]
for tc in range(1, int(input())+1):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            matrix[x+i][y+j] = 1

ans = 0
for i in range(100):
    ans += sum(matrix[i])
print(ans)