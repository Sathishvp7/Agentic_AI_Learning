def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    return arr

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         temp = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > temp:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = temp
#     return arr

list_val = [4,2,6,5,1,3]
print(insertion_sort(list_val))