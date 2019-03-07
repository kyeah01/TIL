record = [list(map(float, input().split())) for _ in range(5)]
total = sum([x[1]-x[0]-1 if x[1]-x[0]<=5 else 4 for x in record if x[1]-x[0]>1])

if total >= 15:
    print(int(total * 10000 * 0.95))
elif total <= 5:
    print(int(total * 10000 * 1.05))
else: 
    print(int(total * 10000))