import sys
sys.stdin = open('3.txt')

def heapify(item, i):
    global heap
    heap += [item]
    j = i
    while j//2:
        if heap[j//2] > heap[j]:
            heap[j//2], heap[j] = heap[j], heap[j//2]
        j //= 2

for tc in range(1, int(input())+1):
    n = int(input())
    nums = list(map(int, input().split()))
    heap = [0]
    i = 1
    for item in nums:
        heapify(item,i)
        i += 1
    i -= 1
    result = 0
    while i//2:
        result += int(heap[i//2])
        i //= 2

    print(f'{tc}', result)