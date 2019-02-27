M = int(input())
mo = [input() for _ in range(M)]
P = int(input())
pattern = [input() for _ in range(P)]
print(mo, pattern)

cnt = 0
for i in range(M-P+1):
    for j in range(M-P+1):
        if mo[i][j:j+P] == pattern[0] and mo[i+1][j:j+P] == pattern[1] and mo[i+2][j:j+P] == pattern[2]:
            cnt += 1
print(cnt)