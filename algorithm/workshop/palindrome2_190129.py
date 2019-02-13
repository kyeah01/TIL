import sys
sys.stdin = open('palindrome2_190129.txt')

def palindrome(lists):
    result = []
    for m in range(100,1,-1):
        for x in range(100):
            for y in range(100-m+1):
                if lists[x][y] == lists[x][y+m-1]:
                    for i in range(m//2+1):
                        if lists[x][y+i] != lists[x][y-i+m-1]:
                            break
                    else:
                        return lists[x][y:y+m]
                        # return m
                if lists[y][x] == lists[y+m-1][x]:
                    for i in range(m//2+1):
                        if lists[y+i][x] != lists[y-i+m-1][x]:
                            break
                    else:
                        # return m
                        for i in range(m):
                            result += lists[y+i][x]
                        return result


T = 10

for tc in range(1, T+1):
    a = input()
    lists = [input() for x in range(100)]
    print(palindrome(lists))