M = int(input())
mo = [input() for _ in range(M)]
P = int(input())
pattern = [input() for _ in range(P)]


cnt = 0
for i in range(M-P+1):
    for j in range(M-P+1):
        for x in range(P):
            if mo[i+x][j:j+P] != pattern[x]:
                break
        else:
            cnt += 1
print(cnt)

# 플래그 사용해서 문제풀기
# cnt = 0
# for i in range(M-P+1):
#     for j in range(M-P+1):
#         flag = 0
#         for x in range(P):
#             if mo[i+x][j:j+P] != pattern[x]:
#                 flag = 1
#                 break
#         if flag != 1:
#             cnt += 1
# print(cnt)