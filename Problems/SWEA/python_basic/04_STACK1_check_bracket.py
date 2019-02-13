T = int(input())

def bracket(String):
    check = { ')' : '(' , '}' : '{' , ']' : '[' }
    h = []
    for i in range(len(String)):
        if String[i] in check.values():
            h.append(String[i])
        elif String[i] in check.keys():
            if len(h) == 0:
                return 0
            elif h[-1] == check[String[i]]:
                h.pop()
            else:
                return 0
    if len(h) == 0:
        return 1
    else:
        return 0

for tc in range(1, T + 1):
    S = input()
    print(f'#{tc}', bracket(S))