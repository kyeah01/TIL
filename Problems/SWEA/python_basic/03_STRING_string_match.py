import sys
sys.stdin = open('190129_string_match_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    str2 = input()
    str1 = input()
    for i in range(len(str1)):
        if str1[i] == str2[0]:
            if str1[i:i+len(str2)] == str2:
                print(f'#{test_case} 1')
                break
            else:
                continue
        else:
            continue
    else:
        print(f'#{test_case} 0')