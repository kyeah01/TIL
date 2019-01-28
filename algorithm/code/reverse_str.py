def reverse_str(str_a):
    list_a = ' '.join(str).split()
    for i in range(len(list_a)//2):
        list_a[i], list_a[-i] = list_a[-i], list_a[i]
    return ''.join(list_a)

print(reverse_str('abc'))


def strcpm(str1, str2):
    i = 0
    if len(str1) != len(str2):
        return False
    else:
        while i < len(str1) and i < len(str2):
            if str1[i] != str2[i]:
                return False
            i += 1
    return True


def atoi(string):
    value = 0
    i = 0
    while (i < len(string)):
        c = string[i]
        if c >= '0' and c <= '9':
            digit = ord(c) - ord('0')
        else:
            break
        value = (value * 10) + digit
        i += 1
    return value

a = '123'
print(type(a))
b = atoi(a)
print(type(b))

str1 = "abc 1,2 ABC"
print(str1)
str1 = str1.replace("1,2", "one, two")
print(str1)


def itoa(intN):
    lists = []
    while intN in list(range(10)):
        lists.insert(intN % 10)
        intN = intN//10
    return ''.join(lists)


def itoa(x):
    str = list()
    y = 0