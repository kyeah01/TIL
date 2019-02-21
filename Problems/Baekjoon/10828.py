def push(x):
    global stack
    stack += [x]

def pop():
    return stack.pop() if stack else -1

def size():
    return len(stack)

def empty():
    return 0 if stack else 1

def top():
    return stack[-1] if stack else -1

T = int(input())
stack = []
for _ in range(T):
    do = input().split()
    if do[0] == 'push':
        push(int(do[1]))
    elif do[0] == 'pop':
        print(pop())
    elif do[0] == 'size':
        print(size())
    elif do[0] == 'empty':
        print(empty())
    elif do[0] == 'top':
        print(top())