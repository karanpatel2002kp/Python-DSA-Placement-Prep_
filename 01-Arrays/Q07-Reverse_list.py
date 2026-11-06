# Input:
# nums = [10, 20, 30, 40, 50]

# Output:
# [50, 40, 30, 20, 10]


nums = [10, 20, 30, 40, 50]
reversed_list = []

for i in range(4,-1,-1):
    reversed_list.append(nums[i])

print(reversed_list)



# Concepts Used:
# Lists
# For Loop
# Range
# Indexing
# Append()
