def bubble_sort(list1):
    for i in range(len(list1)-1,0,-1):
        for j in range(i):
            if list1[j] > list1[j+1]:
                # temp = list1[j]
                # list1[j] = list1[j+1]
                # list1[j+1] = temp
                list1[j], list1[j+1] = list1[j+1], list1[j]
        print(list1)
    return list1


list_val = [4,2,6,5,1,3]
print(bubble_sort(list_val))