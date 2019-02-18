# import sys
# sys.stdin = open('04_min_sum.txt')

# def sumit(N):
#     global minsum
#     donot = set()
#     i = 0
#     sumN = 0
#     while len(donot) != N: 
#         for j in range(N):
#             if j not in donot:
#                 sumN += A[i][j]
#                 donot.update(j)
#             if sumN > minsum:
#                 break
#         else:
#             minsum = sumN
#         i = 0 if i == N-1 else i+1
    

# for tc in range(1, int(input())+1):
#     N = int(input())
#     A = [list(map(int,input().split())) for i in range(N)]
#     minsum = 0
#     print()



def permute(l):
    n = len(l)
    result = []
    c = n * [0]
    result.append(l)

    i = 0
    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                l[0], l[i] = l[i], l[0]
            else:
                l[c[i]], l[i] = l[i], l[c[i]]
            result.append(l[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result

l = [1, 2, 3]
print(permute(l))