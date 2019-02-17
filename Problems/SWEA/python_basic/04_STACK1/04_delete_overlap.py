T = int(input())
for tc in range(1, T + 1):
    S = list(input())
    while True:
        for s in range(len(S)-1):
            if S[s] == S[s+1]:
                S.pop(s)
                S.pop(s)
                break
        else:
            break
    print(f'#{tc}', len(S))