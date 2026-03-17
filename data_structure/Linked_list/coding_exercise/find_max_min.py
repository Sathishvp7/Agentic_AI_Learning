def find_max_min(my_list):
    min_index = 0
    max_index = 0

    for i in range(1,len(my_list)):
        if my_list[i] < my_list[min_index]:
            min_index = i
        if my_list[i] > my_list[max_index]:
            max_index = i

    return (my_list[max_index],my_list[min_index])
    


print( find_max_min([5, 3, 8, 1, 6, 9]) )


"""
    EXPECTED OUTPUT:
    ----------------
    (9, 1)
    
"""