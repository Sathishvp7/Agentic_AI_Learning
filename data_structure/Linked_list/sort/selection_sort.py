"""
Takeaways: Unstable sort but minimal swaps.
what is Unstable 
[4, 2, 4, 3]

Original positions:
index 0 → 4
index 2 → 4

After sorting 
index 0 swap between index3, no second 4 comes first, that why we saying unstable

# Note 
Algorithms like:
Merge Sort
Insertion Sort
Bubble Sort
are stable.

"""

def selection_sort(list1):
    for i in range(len(list1)-1):
        min_index = i
        for j in range(i+1,len(list1)):
            if list1[j] < list1[min_index]:
                min_index = j
        if min_index != i:
            # temp = list1[i]
            # list1[i] = list1[min_index]
            # list1[min_index] = temp
            list1[i], list1[min_index] = list1[min_index], list1[i]
        print(list1)
    return list1

list_val = [4,2,6,5,1,3]
print(selection_sort(list_val))