def combination(n,r,q):
    global result
    if r == 0:
        myprint(q)
    else:
        if n < r:
            return
        else:
            T[r-1] = A[r-1]
            combination(n-1, r-1, q)
            combination(n-1, r, q)
