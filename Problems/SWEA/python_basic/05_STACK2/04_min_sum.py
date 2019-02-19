import sys
sys.stdin = open('04_min_sum.txt')


# n개의 수를 나열하면 n자리의 수와 같다는 발상으로 바로 다음 수를 구하는 코딩.
# 스왑해가면서 가장 작은수부터 가장 큰 수까지 구하면서 순열을 구함.
# def next_perm():
#     global L, N
#     i = N
#     A = L[:]
#     while i > 1:
#         i -= 1
#         if L[i-1] < L[i]:
#             j = i
#             while j < N:
#                 if L[i-1] < L[j]:
#                     k = j
#                 j += 1
#             L[i-1], L[k] = L[k], L[i-1]
#             L = L[:i] + L[i:][::-1]
#             return L if L != A else None

# 구해진 순열을 가지고 matrix에서 값을 구해 sum하는 함수, minimum sum보다 넘어가는 순간 break
# def sumit():
#     global minsum, N, L
#     sumN = 0
#     while L:
#         for i in range(N):
#             sumN += A[i][L[i]]
#             if sumN > minsum:
#                 break
#         else:
#             minsum = sumN
#         sumN = 0
#         L = next_perm()
#     return minsum
    

# for tc in range(1, int(input())+1):
#     N = int(input())
#     A = [list(map(int,input().split())) for i in range(N)]
#     L = list(range(N))
#     minsum = 10000000000000
#     print(sumit())

# 이 방식은 순열을 무조건 다 구하기때문에 시간에러가 났다.


# def recurse(row, n):
#     global mean
#     row += 1
#     currentsum = sum(boards[key][value] for key, value in enumerate(answersheet[0:row])) 
#     if currentsum > mean:
#         return
#     if row == n:
#         if currentsum < mean:
#             mean = currentsum
#     for column in range(n):
#         if column not in answersheet[0:row]:
#             answersheet[row] = column
#             recurse(row, n)
# for tc in range(int(input())):
#     n = int(input())
#     boards = [list(map(int, input().split())) for _ in range(n)]
#     answersheet = [-1] *n
#     row = -1
#     mean = 999
#     recurse(row, n)
#     print(f"#{tc+1} {mean}")


def arr_min_sum(n, row):
    global min_sum
    row += 1
    sumN = sum(A[i][L[i]] for i in range(len(L[0:row])))
    if sumN > min_sum:
        return
    if row == n and sumN < min_sum:
        min_sum = sumN
        return
    for c in range(n):
        if c not in L[0:row]:
            L[row] = c
            arr_min_sum(n, row)


for tc in range(1, int(input())+1):
    N = int(input())
    A = [list(map(int,input().split())) for i in range(N)]
    L = [-1]*N
    min_sum = 10000000000000
    row = -1
    arr_min_sum(N, row)
    print(min_sum)