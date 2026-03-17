"""
Given an array of integers nums and a target integer target, write a Python function called subarray_sum that finds the indices of a contiguous subarray in nums that add up to the target sum using a hash table (dictionary).

Your function should take two arguments:

nums: a list of integers representing the input array

target: an integer representing the target sum

Your function should return a list of two integers representing the starting and ending indices 
of the subarray that adds up to the target sum. If there is no such subarray, 
your function should return an empty list.

nums = [1, 2, 3, 4, 5]
target = 9
print(subarray_sum(nums, target))  # should print [1, 3]

"""

def subarray_sum(nums, target):
    prefix_map = {0: -1}   # To handle subarrays starting from index 0
    current_sum = 0

    for i, num in enumerate(nums):
        current_sum += num
        compliment = current_sum - target
        if compliment in prefix_map:
            start_index = prefix_map[compliment] + 1
            return [start_index, i]

        prefix_map[current_sum] = i

    return None  # If no subarray found

nums = [-8, 1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )
