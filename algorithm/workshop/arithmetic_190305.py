def inorder(node):
    global result
    if node != 0:
        inorder(int(tree[node][1]))
        inorder(int(tree[node][2]))
        result += [tree[node][0]]

for tc in range(1, 11):
    n = int(input())
    tree = [0]+[input().split()[1:]+[0,0] for _ in range(n)]
    result = []
    stack = []
    inorder(1)
    while result:
        next = result.pop(0)
        if next not in {'+', '-', '/', '*'}:
            stack += [next]
        else:
            if next=='+':
                stack += [int(stack.pop())+int(stack.pop())]
            elif next=='-':
                stack += [-int(stack.pop())+int(stack.pop())]
            elif next=='*':
                stack += [int(stack.pop())*int(stack.pop())]
            else:
                stack += [1/int(stack.pop())*int(stack.pop())]
    print('#{}'.format(tc),int(stack[0]))