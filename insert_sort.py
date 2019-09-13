def insert_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        ele = arr[i]
        while arr[j] > ele and j >= 0:
            arr[i] = arr[j]
            j -= 1
        arr[j + 1] = ele
    return arr


print(insert_sort([]))
print(insert_sort([1]))
print(insert_sort([2, 1]))
print(insert_sort([2, 1, 5, 6, 3, 4, 7]))
