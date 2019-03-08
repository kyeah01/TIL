n = int(input())
arr = list(map(int, input().split()))
cnt, cnt2, maxN = 1, 1, 0
for i in range(n-1):
    if arr[i] <= arr[i+1]:
        cnt += 1
    else:
        cnt = 1
    if arr[i] >= arr[i+1]:
        cnt2 += 1
    else:
        cnt2 = 1
    maxN = max(cnt, cnt2, maxN)
print(maxN)