n = int(input())
count = 0
for _ in range(n):
    a,b = input().split()
    set_a = set(a)
    set_a.update(b)
    if len(set_a)+1 < len(a)+len(b):
        count += 1
print(count)