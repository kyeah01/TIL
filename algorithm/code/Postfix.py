# # 중위표기식을 후위표기식으로 바꾸기 위한 코딩입니다.
# for s in String
#     if s가 숫자면
#         result에 더해줌
#     elif s가 '('면,
#         stack에 append
#     elif s가 닫는괄호면,
#         while stack이 존재하는동안 and stack의 탑이 닫는괄호가 아닐때까지.
#             result에 stack을 pop해서 더해줌.
#         while문을 빠져나오고 나서 닫는괄호를 없애준다.
#     elif s가 산술연산자면
#         # stack 값이 없어지거나, 더 높은 우선순위 연산자를 만날때까지 pop해서 result에 더해줌
#         p에 s의 value(스택의 쌓을지에 여부를 판단하기 위해)를 할당해줌
#         while stack이 존재하고, top이 여는괄호가 아니고, operator의 우선순위가 앞서거나 같은 동안
#             stack에서 pop해서 result에 더해줌
#         스택에서 여는괄호 없애줌.

def Postfix(String):
    operator = {'*':2, '/':2, '+':1, '-':1}
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