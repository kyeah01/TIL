seq = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

import sys

T = int(sys.stdin.readline())
for tc in range(1, T+1):
    count = [0 for _ in range(10)]
    L = sys.stdin.readline().split()
    for s in range(len(seq)):
        count[s] = L.count(seq[s])
        print(seq[s]*count[s], end='').lstrip()