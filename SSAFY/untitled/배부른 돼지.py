Y = []
N = []

for tc in range(int(input())):
    t, q = input().split()
    if q == 'N':
        N += [t]
    else:
        Y += [t]
if not Y or not N or min(Y) <= max(N):
    print('F')
else:
    print(int(min(Y)))