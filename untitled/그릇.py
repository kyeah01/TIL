inp = input()
cnt = 0
for i in range(len(inp)-1):
    if inp[i] == inp[i+1]:
        cnt += 5
    else:
        cnt += 10
cnt += 10
print(cnt)