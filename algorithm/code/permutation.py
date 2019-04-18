def permutation(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used):
        # 2.
        if len(chosen) == r:
            print(chosen)
            return
	
	# 3.
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
    generate([], used)


permutation('ABCD', 2)
permutation([1, 2, 3, 4, 5], 3)



def myprint(n):
    for i in range(n):
        print(" %d" % (a[i]), end="")
    print()
def perm(n, k):
    if n == k:
        myprint(n)
    else:
        for i in range(k, n):
            a[i], a[k] = a[k], a[i]
            perm(n, k+1)
            a[i], a[k] = a[k], a[i]

a = [1, 2, 3, 4]
perm(4, 0)

