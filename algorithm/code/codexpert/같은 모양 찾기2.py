M = int(input())
mo = [input() for _ in range(M)]
P = int(input())
pattern = [input() for _ in range(P)]
pattern = [list(x) for x in pattern]
pat1 = [[pattern[i][j] for i in range(P-1, -1, -1)] for j in range(P)]
pat2 = [[pat1[i][j] for i in range(P-1, -1, -1)] for j in range(P)]
pat3 = [[pat2[i][j] for i in range(P-1, -1, -1)] for j in range(P)]

pattern = [''.join(x) for x in pattern]
pat1 = [''.join(x) for x in pat1]
pat2 = [''.join(x) for x in pat2]
pat3 = [''.join(x) for x in pat3]


cnt = 0
for i in range(M-P+1):
    for j in range(M-P+1):
        for x in range(P):
            if mo[i+x][j:j+P] != pattern[x]:
                break
        else:
            cnt += 1
        for x in range(P):
            if mo[i+x][j:j+P] != pat1[x]:
                break
        else:
            cnt += 1
        for x in range(P):
            if mo[i+x][j:j+P] != pat2[x]:
                break
        else:
            cnt += 1
        for x in range(P):
            if mo[i+x][j:j+P] != pat3[x]:
                break
        else:
            cnt += 1
print(cnt)