s,x = input().split()
s = list(s)
for i in range(1, len(s)):
    if int(''.join(s[:i])) + int(''.join(s[i:])) == int(x):
        print(f'{int("".join(s[:i]))}+{int("".join(s[i:]))}={x}')
        break
else:
    print('NONE')