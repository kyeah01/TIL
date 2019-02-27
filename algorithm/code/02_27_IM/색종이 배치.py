ax, ay, ar, ac = map(int, input().split())
bx, by, br, bc = map(int, input().split())

x = set(range(ax, ax+ar+1)) & set(range(bx, bx+br+1))
y = set(range(ay, ay+ac+1)) & set(range(by, by+bc+1))

if len(x) == 1 and len(y) == 1:
    print(1)
elif len(x) == 1 or len(y) == 1:
    print(2)
elif len(x) and len(y):
    print(3)
else:
    print(4)