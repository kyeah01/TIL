def hap(num):
    while num >= 10:
        num = num//10 + num%10
    return num

sol = 0
for _ in range(int(input())):
    ans = 0
    num = int(input())
    if hap(sol) < hap(num):
        sol = num
    elif hap(sol) == hap(num):
        sol = min(num, sol)
print(sol)