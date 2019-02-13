import sys
sys.stdin = open('190129_count_letter_input.txt')

T = int(input())

for tc in range(1,T+1):
    str1 = set(input())
    str2 = '_'.join(input()).split('_')
    dict1 = {i:0 for i in str1}
    for j in str2:
        for i in str1:
            if i == j:
                dict1[i] += 1
    # dict1 = {i:str2.count(i) for i in str1}
    print(f'#{tc} {max(dict1.values())}')