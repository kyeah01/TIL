# def counting_sort(arrange):
#     A = range(10)
#     for i in A:
#         if arrange(i) == i:
#             A[i] += 1
#     return A


def counting_sort(A):
    B = [0]*len(A)
    C = [0]*10
    for i in range(len(A)):
        C[A[i]] += 1
    for i in range(1, len(C)):
        C[i] += C[i-1]
    for i in range(len(B)-1,-1,-1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= -1
    return B

A = [1,4,5,1,2,4,5,7,9,3]
print(counting_sort(A))