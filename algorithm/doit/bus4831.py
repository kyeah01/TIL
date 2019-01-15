T = int(input())
for i in range(T):
    K, N, M = map(int,input().split())
    busstop = list(map(int,input().split()))
    count = 0
    ox = [0]*(N+1)
    for x in busstop:
        ox[x] = 1
    busstop =[0] + busstop + [N]
    charge = K
    while True:
        if ox[charge] != 1:
            charge -= 1
        elif ox[charge] == 1:
            count += 1
            ox = ox[charge:]
            charge = K
            if len(ox) <= K:
                break
        if charge == 0:
            count = 0
            break
    print(f'#{i+1} {count}')


# 존재할때마다 더하는 알고리즘을 짰으나 중복을 제거할 수 없었다.
# for x in range(len(busstop)-1):
#         if busstop[x] + K < busstop[x+1]:
#             ans = 0
#             break
#         else:
# else:
#     for q in range(1,N):
#         try:
#             if busstop[x] + K >= busstop[x+1+q]:
#                 count -= q
#         except IndexError:
#             continue

    # for x in range(len(busstop)-2):
    # if busstop[x] + K < busstop[x+1]:
    #     ans = 0
    #     break
    # else:
    #     for y in range(1, N-x):
    #         if busstop[x] + K >= busstop[x+y+1]:
    #             count -= y

    # p = N+1
    # while True:
    #     try:
    #         if busstop[x] + K >= busstop[x+1+p]:
    #             count -= p
    #         p -= 1
    #     except IndexError:
    #         break



    