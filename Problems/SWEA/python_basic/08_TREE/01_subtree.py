import sys
sys.stdin = open('1.txt')

for tc in range(1, int(input())+1):
    count_Edge, target = map(int, input().split())
    inp = list(map(int, input().split()))
    inp = [inp[i-1:i+1] for i in range(len(inp)) if i%2]
    Edge = [[i,0,0,0] for i in range(count_Edge+2)]
    for i in range(count_Edge+2):
        for j in range(count_Edge):
            if inp[j][0] == Edge[i][0]:
                if Edge[i][1]:
                    Edge[i][2] = inp[j][1]
                else:
                    Edge[i][1] = inp[j][1]
            if inp[j][1] == Edge[i][0]:
                Edge[i][3] = inp[j][0]

    target = [target]
    did_it = []
    while target:
        t = target.pop(0)
        if t not in did_it:
            for i in range(count_Edge+2):
                if Edge[i][3] == t:
                    target += [i]
        else:
            break
        did_it += [t]

    print(len(did_it))