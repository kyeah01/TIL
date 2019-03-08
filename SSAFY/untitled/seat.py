C, R = map(int, input().split())
K = int(input())

if K > C*R:
    print(0)
else:
    i,j = C,R-1
    chk = 0
    while K > chk and j and j:
        chk += i
        i -= 1
        if K <= chk:
            break
        chk += j
        j -= 1