def bubble_sort(arr):
    change = True
    while change:
        change = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                change = True
    return arr


print(bubble_sort([]))
print(bubble_sort([1]))
print(bubble_sort([2, 1]))
print(bubble_sort([2, 1, 5, 6, 3, 4, 7]))
