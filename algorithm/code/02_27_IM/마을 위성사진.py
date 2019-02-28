N = int(input())
sat = [list(map(int, input())) for _ in range(N)]


# while True:
#     chk = 0
#     for i in range(1, N-1):
#         for j in range(1, N-1):
#             if sat[i][j]:
#                 print(i,j)
#                 for d in range(4):
#                     if not sat[i+de[d]][j+de[::-1][d]]:
#                         break
#                 else:
#                     if abs(sat[i][j]-sat[i][j-1]) == 1:
#                         sat[i][j] += 1
#                         chk = 1
#     if chk == 0:
#         break
# print(sat)
#
# for i in range(N):
#     for j in range(N):
#         if sat[i][j] == 1:
#             cnt = 1
#             for k in range(1, N):
#                 if sat[i][j+k]:
#                     cnt += 1
#                 else:
#                     break
#             sat[i][j:j+cnt] = list(range(1, (cnt+1)//2)+1) + list(range(1, (cnt)//2)+1)[::-1]

v = 1
a = 10
while v != a:
    chk = 0
    a = v
    for i in range(1, N-1):
        for j in range(1, N-1):
            if sat[i][j] and v == 1 or sat[i][j] == v:
                m = min(sat[i - 1][j], sat[i + 1][j], sat[i][j - 1], sat[i][j + 1])
                if sat[i][j] <= m:
                    sat[i][j] = m+1
                    v = max(m+1, v)

for s in sat:
    print(*s)
print(v)
