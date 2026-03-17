# Here we going to do 2 steps
 #Step1 - Merge function --> 2 parameters List1 and List2
    # Assumption --> Both List 1 and List 2 is sorted respectively

def merge(list1, list2):
    combined = []
    i = 0 #initilaizse list 1 index
    j = 0 # initializse List2 index

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1

    while i < len(list1):
        combined.append(list1[i])
        i += 1
        
    while j < len(list2):
        combined.append(list2[j])
        j += 1

    return combined

list1 = [2,4,6,8,10]
list2 = [1,3,5,7,9]

print(merge(list1,list2))


def merge_sort(list1):
    # divide list
    if len(list1) == 1:
        return list1
    mid_index = len(list1) // 2
    # recursion
    left =  merge_sort(list1[:mid_index])
    right = merge_sort(list1[mid_index:])

    return merge(left,right)


list1 = [4,2,6,5,1,3]

print(merge_sort(list1))
