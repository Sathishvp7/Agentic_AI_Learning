# Method 1 - Nested For loop so O(n²)
def item_in_common(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

list1 = [1,3,5]
list2 = [2,4,6]

print(item_in_common(list1, list2))

# Method 2 - Optimizsed approach  - O(2n) = O(n)
def item_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True
    print(my_dict)
    for j in list2:
        if j in my_dict:
            return True

    return False


list1 = [1,3,5]
list2 = [2,4,6]


print(item_in_common(list1, list2))

