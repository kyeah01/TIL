def bubble_sort(data):
    for i in range(len(data)-1,0,-1):
        for j in range(0,i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data


data= [55, 7, 78, 12, 42]
print(bubble_sort(data))