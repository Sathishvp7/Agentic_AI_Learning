# # Find Pivot

# arr = [8,3,1,7,0,10,2]
# # Objective is Use First item as Pivot and make left and right
# # Left will have less than 8 and right greater than 8, center will be 8
# pivot_index = 0
# swap_index = 0

# for i in range(1,len(arr)):
#     if arr[i] < arr[pivot_index]:
#         swap_index += 1
#         arr[i], arr[swap_index] = arr[swap_index], arr[i]
    
# arr[pivot_index], arr[swap_index] = arr[swap_index], arr[pivot_index]
# print(arr)



# def pivot(my_list,start,end):
#     pivot_index = start
#     swap_index = start

#     for i in range(pivot_index + 1, end):
#         if my_list[pivot_index] > my_list[i]:
#             swap_index += 1
#             # swap
#             my_list[swap_index], my_list[i] = my_list[i], my_list[swap_index]
    
#     # swap
#     my_list[pivot_index], my_list[swap_index] = my_list[swap_index], my_list[pivot_index]
#     print(my_list)
#     left_arr = my_list[:swap_index]
#     right_arr = my_list[swap_index+1:]
#     print(left_arr, right_arr)
#     return swap_index

# arr = [8,3,1,7,0,10,2]
# center_index = pivot(arr,0, len(arr))



def pivot(my_list, start,end):
    pivot_index = start
    swap_index = start

    for i in range(pivot_index + 1, end):
        if my_list[pivot_index] > my_list[i]:
            swap_index += 1
            my_list[swap_index], my_list[i] = my_list[i], my_list[swap_index]
    
    print(f'Pivot before Swap {my_list}')
    my_list[pivot_index], my_list[swap_index] = my_list[swap_index], my_list[pivot_index]
    print(f'After Swap pivot index {my_list}')

    return swap_index

def quick_sort_helper(my_list, left, right):
    if left < right:
        index = pivot(my_list, left, right)
        quick_sort_helper(my_list, 0, index)
        quick_sort_helper(my_list, index+1, right)
    return my_list

def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list))


# arr = [8,3,1,7,0,10,2]
# quick_sort_result = quick_sort(arr)
# print(quick_sort_result)


# Method 2 - Much similar but quite readable


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # Select Pivot - Last value as pivot
    pivot = arr[-1]
    left = []
    right = []

    for i in arr[:-1]:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)
    
    print(left, right)
    return quick_sort(left) + [pivot] + quick_sort(right) # Ascending Order
    #return quick_sort(right)  + [pivot] + quick_sort(left) # descending order

arr = [8,3,1,7,0,10,2]
quick_sort_result = quick_sort(arr)
print(quick_sort_result)
















