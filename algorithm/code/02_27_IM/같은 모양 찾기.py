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