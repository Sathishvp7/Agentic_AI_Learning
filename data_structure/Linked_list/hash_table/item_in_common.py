"""
HT: Item In Common ( ** Interview Question)
Write a function item_in_common(list1, list2) that takes two lists as input and returns True if there is at least one common item between the two lists, False otherwise.
"""

def item_in_common(list1,list2):
    new_dict = {}
    
    for i in list1:
        new_dict[i] = True
    
    for j in list2:
        if j in new_dict:
            return True
    
    return False

list1 = [1,3,5]
list2 = [2,4,5]


print(item_in_common(list1, list2))

"""
    EXPECTED OUTPUT:
    ----------------
    True

"""