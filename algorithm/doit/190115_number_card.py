T = int(input())
for i in range(T):
    N = int(input())
    A = list(map(int,' '.join(input()).split()))
    save = [0]*10
    for x in range(10):
        for y in A:
            if x == y:
                save[x] += 1
    maxN = 0
    number = 0
    for z in range(len(save)):
        if save[z] >= maxN:
            maxN = save[z]
            number = z
    print(f'#{i+1} {number} {maxN}')