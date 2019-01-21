def selection_sort(a):
    for i in range(len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]

data = [64, 25, 10, 22, 11]
selection_sort(data)
print(data)