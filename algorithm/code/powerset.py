def powerset(arr):
    A = [0 for _ in arr]

    def maker(n,k):
        if n == k:
            
        else:
            A[k] = 1
            maker(n, k+1)
            A[k] = 0
            maker(n, k+1)
    return maker(len(arr),0)

print(powerset([1,2]))


for k in range(n):
    for i in range(2):
        A[k] = i
        