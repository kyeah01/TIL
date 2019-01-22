import sys
sys.stdin = open("binary_search_input.txt")

def binary_search(P, A, B):
    start = 1
    end = P
    ctA = ctB = 0
    while (start+end)//2 != A:
        if (start+end)//2 < A:
            start = (start+end)//2
            ctA += 1
        elif (start+end)//2 > A:
            end = (start+end)//2
            ctA += 1
    start = 1
    end = P
    while (start+end)//2 != B:
        if (start+end)//2 < B:
            start = (start+end)//2
            ctB += 1
        elif (start+end)//2 > B:
            end = (start+end)//2
            ctB += 1
    if ctA == ctB:
        return 0
    elif ctA > ctB:
        return 'B'
    else:
        return 'A'


T = int(input())
for tc in range(T):
    P, A, B = map(int, input().split())
    print(f'#{tc+1}',binary_search(P, A, B))