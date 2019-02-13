for i in range(10):
    C = int(input())
    Dump = list(map(int,input().split()))
    maxN = minN = 0
    for x in range(C):
        for y in range(len(Dump)):
            if Dump[y] > Dump[maxN]:
                maxN = y
            if Dump[y] < Dump[minN]:
                minN = y
        Dump[maxN] -= 1
        Dump[minN] += 1
    
    for number in Dump:
        maxN = minN = Dump[0]
        if number > maxN:
            maxN = number
        elif number < minN:
            minN = number
    print(maxN-minN)