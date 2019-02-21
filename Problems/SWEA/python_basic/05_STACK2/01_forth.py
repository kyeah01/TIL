import sys
sys.stdin = open('01_forth.txt') 

for tc in range(1, int(input())+ 1):
    L = input().split()
    stack = []
    for t in L:
        if t not in {'+', '-', '/', '*', '.',}:
            stack += [t]
        elif t == '.':
            if len(stack) == 1:
                print(f'#{tc}', stack[0])
            else:
                print(f'#{tc}', 'error')
                break
        else:
            try:
                if t == '+':
                    stack += [int(stack.pop()) + int(stack.pop())]
                elif t == '-':
                    stack += [-int(stack.pop()) + int(stack.pop())]
                elif t == '*':
                    stack += [int(stack.pop()) * int(stack.pop())]
                elif t == '/':
                    stack += [int(1/int(stack.pop()) * int(stack.pop()))]
            except IndexError:
                print(f'#{tc}', 'error')
                break