def ssum(n):
    if n == 1:
        return 1
    else:
        return n+ssum(n-1)

def find_max(Lists):
    n = len(Lists)