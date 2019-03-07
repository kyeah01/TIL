for tc in range(1, int(input())+1):
    n, k_min, k_max = map(int, input().split())
    people = list(map(int, input().split()))
    scores = sorted(list(set(people)))
    ans, minN = 0,10000000
    flag = False
    for T1 in scores:
        for T2 in scores:
            arr1, arr2, arr3 = 0,0,0
            for person in people:
                if person < T1:
                    arr1 += 1
                elif person < T2:
                    arr2 += 1
                else:
                    arr3 += 1
                if max(arr1, arr2, arr3) > k_max:
                    break
            if k_min <= min(arr1, arr2, arr3) and max(arr1, arr2, arr3) <= k_max:
                flag = True
                minN = min(minN, max(arr1, arr2, arr3)-min(arr1, arr2, arr3))
    print(minN) if flag else print(-1)