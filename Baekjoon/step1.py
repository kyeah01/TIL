# A = 33
# B = "kyeah01"

# print(A,B)


# # ?. 그대로 출력하기

# import sys
# A = "시작!"

# while bool(A):
#     A = sys.stdin.read()
#     if bool(A) == False : break
#     print(A)

# 8958. OX 퀴즈

import sys

N = int(input())
a = 0
s = 0
T = []

while N:
    A = sys.stdin.readline()
    N -= 1
    for i in range(len(A)):
        if A[0] != 'O':
            if A[i] == 'O' and A[i+1] == 'O' or i == 0:
                a += 1
                T.append(a)
            if A[i] == 'O':
                s += a
        else:
            a = 1
            if A[i] == 'O':
                s += a
    print(a,s)
    print(T)
    s = a = 0
    if N == 0: break
print(a,s)
print(T)
