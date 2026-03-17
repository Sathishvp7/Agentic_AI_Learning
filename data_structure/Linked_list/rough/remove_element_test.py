# def remove_element(my_list, val):
#     for enu,i in enumerate(my_list):
#         if i == val:
#             my_list.pop(enu)
#     return my_list


def remove_element(my_list,val):
    i=0
    while i < len(my_list):
        if my_list[i] == val:
            my_list.pop(i)
        else:
            i+= 1
    return my_list

my_list = [3,3,3,3]
val = 3

print(remove_element(my_list,val))