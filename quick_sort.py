# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     pivot = arr.pop()
#     left = []
#     center = [pivot]
#     right = []
#     for elem in arr:
#         if elem < pivot:
#             left.append(elem)
#         elif elem > pivot:
#             right.append(elem)
#         else:
#             center.append(elem)
#
#     return quick_sort(left) + center + quick_sort(right)
        

# print(quick_sort([]))
# print(quick_sort([1]))
# print(quick_sort([2, 1]))
# print(quick_sort([2, 1, 5, 6, 3, 4, 7]))
