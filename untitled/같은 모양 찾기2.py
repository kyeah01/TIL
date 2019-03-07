# M = int(input())
# mo = [input() for _ in range(M)]
P = int(input())
pattern = [input() for _ in range(P)]
pattern = [list(x) for x in pattern]
pat1 = [list(x) for x in pattern]
pat2 = [list(x) for x in pattern]
pat3 = [list(x) for x in pattern]

for i in range(P):
    for j in range(P):
        if i-(P-1) <0:
            pat1[i][j] = pattern[0][j-(i-(P-1))]
        else:
            pat1[i][j] = pattern[i-(P-1)][j]

for i in range(P):
    for j in range(P):
        if i-(P-1) <0:
            pat2[i][j] = pat1[0][j-(i-(P-1))]
        else:
            pat2[i][j] = pat1[i-(P-1)][j]

for i in range(P):
    for j in range(P):
        if i-(P-1) <0:
            pat3[i][j] = pat2[0][j-(i-(P-1))]
        else:
            pat3[i][j] = pat2[i-(P-1)][j]

pattern = [''.join(x) for x in pat1]
pat1 = [''.join(x) for x in pat1]
pat2 = [''.join(x) for x in pat2]
pat3 = [''.join(x) for x in pat3]
for x in range(P):
    print(pattern[x])
print()
for x in range(P):
    print(pat1[x][::-1])
print()
for x in range(P):
    print(pat2[x])
print()
for x in range(P):
    print(pat3[x][::-1])


# cnt = 0
# for i in range(M-P+1):
#     for j in range(M-P+1):
#         for x in range(P):
#             if mo[i+x][j:j+P] != pattern[x]:
#                 break
#         else:
#             cnt += 1
#         for x in range(P):
#             if mo[i+x][j:j+P] != pattern[x][::-1]:
#                 break
#         else:
#             cnt += 1
#         for x in range(P):
#             if mo[i+x][j:j+P] != pat[x]:
#                 break
#         else:
#             cnt += 1
#         for x in range(P):
#             if mo[i+x][j:j+P] != pat[x][::-1]:
#                 break
#         else:
#             cnt += 1
# print(cnt)