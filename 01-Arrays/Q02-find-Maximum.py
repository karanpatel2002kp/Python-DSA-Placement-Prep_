# Q2. Find Maximum Element
# Problem statement:

# Given an array of integers, find the largest element in the array.

# Example:
# nums = [12, 45, 7, 89, 23]
# Expected output:
# 89

nums = [12, 45, 7, 89, 23]

def largest_Element(nums):
    max_num = nums[0]
    for index,value in enumerate(nums):
        if value>max_num:
            max_num = value
    return max_num

print(largest_Element(nums))
    
