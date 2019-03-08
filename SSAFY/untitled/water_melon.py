n = int(input())
inp = [list(map(int, input().split())) for _ in range(6)]
field = {i:[] for i in range(1,5)}
for x in inp:
    field[x[0]] += [x[1]]
print(field)
# big = sum(field[1])*sum(field[2])
# small = min(field[1] if len(field)==2 )*min(field[2], field[4])
# print(big-small)