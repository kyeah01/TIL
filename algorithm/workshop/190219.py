def Postfix(String):
    operator = {'*':2, '+':1}
    bracket = {'(', ')'}
    stack = []
    result = []
    for s in String:
        if s not in operator and s not in bracket:
            result += [s]
        elif s == '(':
            stack += [s]
        elif s == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
        elif s in operator:
            while stack and stack[-1] != '(' and operator[s] < operator[stack[-1]]:
                result += stack.pop()
            stack.append(s)
    while stack:
        result += stack.pop()
    return result

def calc(post):
    stack = []
    for t in post:
        if t not in {'+', '*'}:
            stack += [t]
        else:
            if t == '+':
                stack += [int(stack.pop()) + int(stack.pop())]
            elif t == '*':
                stack += [int(stack.pop()) * int(stack.pop())]
    return stack


for tc in range(1, 11):
    input()
    print(f'#{tc}', calc(Postfix(input())))