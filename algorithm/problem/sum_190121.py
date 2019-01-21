import sys
sys.stdin = open("input.txt")

N = int(input())
L = []

for i in range(100):
    L.append(list(map(int,input().split())))

for T in range(10):
    maxJ = 0
    maxI = 0
    maxD = 0
    maxD2 = 0
    sumD = 0
    sumD2 = 0
    for i in range(100):
        sumJ = 0
        sumI = 0
        for j in range(100):
            sumJ += L[i][j]
            sumI += L[j][i]
        if sumJ > maxJ:
            maxJ = sumJ
        if sumI > maxI:
            maxI = sumI
        sumD += L[i][i]
        sumD2 += L[i][99-i]
    if sumD2 > maxD2:
        maxD2 = sumD2
    if sumD > maxD:
        maxD = sumD
    print(max(maxI, maxJ, maxD, maxD2))