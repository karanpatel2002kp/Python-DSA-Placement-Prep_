# Day 6 - Sum of Array Elements

# Question:
# Find the sum of all elements in a given list.

# Input:
# nums = [5, 10, 15, 20, 25]

# Approach:
# 1. Initialize total = 0.
# 2. Traverse each element using a loop.
# 3. Add each element to total.
# 4. Print the final sum.

num = [5,10,15,20,25]

total = 0

for i in range(len(num)):
    total  = total + num[i]
print(total)

