# Using for Loop with enumerate (Problematic)
def remove_element(my_list, val):
    """
    Removes all occurrences of 'val' from the list using a for loop.

    Issue:
    Using pop() while iterating with enumerate can cause elements
    to be skipped because the list shrinks and indexes shift left.
    """
    
    for enu, i in enumerate(my_list):
        if i == val:
            my_list.pop(enu)
            
    return len(my_list)

"""
Why This Approach is Problematic

When pop() removes an element:
    - All elements shift left by one index
    - But enumerate() continues with the next index
    - This causes some elements to never be checked

Example - my_list = [3, 3, 3] and val = 3
Expected - [] but we will get [3]

Reason - First iteration 3 matching so we poping now list will [3,3], but we already processed index 0 so it will skip
 and move next item there 3 so it will remove. and list end so remaining 3 will be output
 which is incorrect.

"""

def remove_element(nums, val):
    """
    Removes all occurrences of 'val' from the list using a while loop.

    Advantage:
    The index is manually controlled. When an element is removed,
    the index is not incremented so the next shifted element is checked.
    """
    
    i = 0
    
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)      # remove element
        else:
            i += 1           # move to next element
            
    return len(nums)


# Test case 1: Removing a single instance of a value (1) in the middle of the list.
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
val1 = 1
print("\nRemove a single instance of value", val1, "in the middle of the list.")
print("BEFORE:", nums1)
new_length1 = remove_element(nums1, val1)
print("AFTER:", nums1, "\nNew length:", new_length1)
print("-----------------------------------")

# Test case 2: Removing a value that's located at the end of the list.
nums2 = [1, 2, 3, 4, 5, 6]
val2 = 6
print("\nRemove value", val2, "that's located at the end of the list.")
print("BEFORE:", nums2)
new_length2 = remove_element(nums2, val2)
print("AFTER:", nums2, "\nNew length:", new_length2)
print("-----------------------------------")

# Test case 3: Removing a value that's located at the start of the list.
nums3 = [-1, -2, -3, -4, -5]
val3 = -1
print("\nRemove value", val3, "that's located at the start of the list.")
print("BEFORE:", nums3)
new_length3 = remove_element(nums3, val3)
print("AFTER:", nums3, "\nNew length:", new_length3)
print("-----------------------------------")

# Test case 4: Attempting to remove a value from an empty list.
nums4 = []
val4 = 1
print("\nAttempt to remove value", val4, "from an empty list.")
print("BEFORE:", nums4)
new_length4 = remove_element(nums4, val4)
print("AFTER:", nums4, "\nNew length:", new_length4)
print("-----------------------------------")

# Test case 5: Removing all instances of a repeated value.
nums5 = [1, 1, 1, 1, 1]
val5 = 1
print("\nRemove all instances of value", val5, "from the list.")
print("BEFORE:", nums5)
new_length5 = remove_element(nums5, val5)
print("AFTER:", nums5, "\nNew length:", new_length5)
print("-----------------------------------")

