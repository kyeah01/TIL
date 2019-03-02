T = int(input())

print(-1) if T%10 else print(T//300, T%300//60, T%300%60//10)