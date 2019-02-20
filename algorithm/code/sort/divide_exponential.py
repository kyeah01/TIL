# 분할정복 알고리즘을 통해 n의 x승을 구현 한 것이다.
# 재귀활용.
# 계산속도가 log2의 n이 된다.

def Power(base, exp):
    if not exp:
        return 0
    elif exp == 1:
        return base
    if exp % 2:
        new_base = Power(base, exp//2)
        return new_base * new_base * base
    else:
        new_base = Power(base, exp//2)
        return new_base * new_base

a = 2
e = 5
print(Power(a,e))