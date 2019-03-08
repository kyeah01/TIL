n = int(input())
lotus = [int(input()) for _ in range(n)]
lotus.sort()
cnt = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        first = lotus[j]-lotus[i]
        for k in range(j+1, n):
            second = lotus[k]-lotus[j]
            if first*2 < second:
                break
            if first <= second <= first*2:
                cnt += 1
print(cnt)