# arr1이 긴 패턴(매칭당해야 하는 텍스트), arr2가 짧은패턴(매칭해야 하는 패턴)일때
def brute_force(arr1, arr2):
    for i in range(len(arr1)):
        if arr1[i] == arr2[0]:
            if arr1[i:i+len(arr2)] == arr2:
                return i,len(arr2)+1
            else:
                continue
        else:
            continue
    else:
        return False

p = 'is'
t = 'This is a book~!'
print(brute_force(t,p))


def Bbit_print(a):
    for i in range(7,-1,-1):
        if a & (1<<i):
            print(1, end='')
        else:
            print(0, end ='')
    print()