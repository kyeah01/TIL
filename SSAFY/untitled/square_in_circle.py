R = int(input())

cnt = 0
for i in range(1, R):
    for j in range(1, R):
        if i**2 + j**2 <= R**2:
            cnt += 1
print(4*cnt)