"""
List: Max Sub Array ( ** Interview Question)
Given an array of integers nums, write a function max_subarray(nums) 
that finds the contiguous subarray (containing at least one number) with the largest sum and returns its sum.
"""

def max_subarray(nums):
    # Return 0 if input list is empty
    if not nums:
        return 0
 
    # Initialize max_sum and current_sum
    max_sum  = nums[0]
    current_sum = nums[0]
 
    # Iterate through the remaining elements
    for num in nums[1:]:
        # Update current_sum
        current_sum = max(num, current_sum + num)
        # Update max_sum if current_sum is larger
        max_sum = max(max_sum, current_sum)


# Example 1: Simple case with positive and negative numbers
input_case_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result_1 = max_subarray(input_case_1)
print("Example 1: Input:", input_case_1, "\nResult:", result_1)  