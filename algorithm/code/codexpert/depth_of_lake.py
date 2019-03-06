N = int(input())
sat = [list(map(int, input().split())) for _ in range(N)]
v = 1
a = 10
for i in range(1, N-1):
    for j in range(1, N-1):
        if sat[i][j]:
            cnt1, cnt2, cnt3, cnt4 = 0,0,0,0
            x1,x2,y1,y2 = i,i,j,j
            while sat[x1][j]:
                x1 -= 1
                cnt1 += 1
            while sat[x2][j]:
                x2 += 1
                cnt2 += 1
            while sat[i][y1]:
                y1 -= 1
                cnt3 += 1
            while sat[i][y2]:
                y2 += 1
                cnt4 += 1
            v = min(cnt1, cnt2, cnt3, cnt4)
            sat[i][j] = v

sumN = 0
for s in sat:
    sumN += sum(s)
print(sumN)