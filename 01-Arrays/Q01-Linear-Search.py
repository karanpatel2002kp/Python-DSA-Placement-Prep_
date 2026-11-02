# ==========================================
# DSA Day 1 - Question 1
# Topic: Arrays - Linear Search
# ==========================================

# Problem Statement:
# Given a list of numbers and a target value,
# find the index of the target element.
#
# If the target is not present, return -1.

# Example 1:
# Input:
# nums = [5, 12, 8, 20, 15]
# target = 8
#
# Output:
# 2

# Example 2:
# Input:
# nums = [10, 20, 30, 40]
# target = 50
#
# Output:
# -1

# Approach:
# 1. Check each element one by one.
# 2. Compare the element with the target.
# 3. If target is found, return its index.
# 4. If target is not found, return -1.

# Time Complexity: O(n)
# Space Complexity: O(1)

#Input:
nums = [5, 12, 8, 20, 15]
target = 8
#output : 2

def linear_search(nums,target):

    for index,value in enumerate(nums):
        if value == target:
            return index
    return -1

#fn call
result = linear_search(nums,target)
print(result)
