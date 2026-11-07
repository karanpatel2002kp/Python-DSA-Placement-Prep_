#  Remove Duplicates from List
# Problem
# Given a list of integers, remove duplicate elements while maintaining the original order of elements.
# Example
# Input:
# nums = [5, 5, 10, 10, 15, 20, 20, 25]

# Output:
# [5, 10, 15, 20, 25]

# Approach
# Create an empty list called unique.
# Iterate through the original list using a for loop.
# Check whether the current element is already present in unique.
# If it is not present, add it using append().
# Print the final list.

# Python Code
nums = [1, 2, 2, 3, 4, 4, 5]
unique_list = []

for num in nums:
    if num not in unique_list:
        unique_list.append(num)
print(unique_list)     


# Learning Outcome
# Learned how to remove duplicate elements from a list while preserving the original order using Python.
