#2750. 수 정렬하기
N = int(input())

A = [int(input()) for i in range(N)]
A.sort()
for i in A:
    print(i)

#2751. 수 정렬하기2

N = int(input())
A = [int(input()) for i in range(N)]
A.sort()
print(A[::-1], end='\n')

x = int(input())

