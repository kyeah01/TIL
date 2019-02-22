import sys

R, C, ZR, ZC = map(int, sys.stdin.readline().split())

result = [''.join(list(map(lambda x:x*ZC, input()))) for _ in range(R)]

for x in result:
    for _ in range(ZR):
        print(x)