#  Sum of Even Numbers in a List 
# Problem Statement
# Given a list of numbers, calculate the sum of all even numbers in the list.

# Input
# nums = [2, 5, 8, 3, 10]

# Expected Output
# 20

nums = [2, 5, 8, 3, 10]
total = 0
for num in nums:
    if num % 2 == 0:
        total += num
print(total)