def snail(h, up, down):
    answer = cnt = 0
    while answer <= h:
        answer += up
        cnt += 1
        if answer >= h:
            return cnt
        else:
            answer -= down

print(snail(100,5,2))