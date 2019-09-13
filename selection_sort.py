def selection_sort(arr):
    res = []
    while len(arr) > 0:
        min_index = None
        for i, elem in enumerate(arr):
            if min_index is None or arr[min_index] > elem:
                min_index = i
        res.append(arr.pop(min_index))
    return res


print(selection_sort([]))
print(selection_sort([1]))
print(selection_sort([2, 1]))
print(selection_sort([2, 1, 5, 6, 3, 4, 7]))
