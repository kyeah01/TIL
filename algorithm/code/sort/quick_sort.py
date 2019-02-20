# def QuickSort(L, start, end):
#     if start < end:

def quick_sorted(arr):
    if len(arr) > 1:
        pivot = arr[len(arr)-1]
        left, mid, right = [], [], []
        for i in range(len(arr)-1):
            if arr[i] < pivot:
                left.append(arr[i])
            elif arr[i] > pivot:
                right.append(arr[i])
            else:
                mid.append(arr[i])
        mid.append(pivot)
        return quick_sorted(left) + mid + quick_sorted(right)
    else:
        return arr
        
arr = [3, 5, 1, 2, 9, 6, 4, 7, 5]
print(quick_sorted(arr))