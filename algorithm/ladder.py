for _ in range(10):
    tc = input()
    matrix = [0]*100
    for q in range(100):
        matrix[q] = list(map(int, input().split()))

    for w in range(100):
        if matrix[99][w] == 2:
            end = w
            break

    i = 98
    j = end
    while i > 0:
        if j == 99:
            if matrix[i][j-1]:
                while j != 0 and matrix[i][j-1] != 0:
                    j -= 1
                i -= 1
            else:
                i -= 1
        elif j:
            if matrix[i][j-1]:
                while j != 0 and matrix[i][j-1] != 0:
                    j -= 1
                i -= 1
            elif matrix[i][j+1]:
                while j != 99 and matrix[i][j+1] != 0:
                    j += 1
                i -= 1
            else:
                i -= 1
        else:
            if matrix[i][j+1]:
                while j != 99 and matrix[i][j+1] != 0:
                    j += 1
                i -= 1
            else:
                i -= 1
    print(j)
    