# Q8. Extract Even Numbers
# Problem: Create a new list containing only even numbers from the given list.

# Input:
# nums = [5, 10, 15, 20, 25, 30]

# Output:
# [10, 20, 30]


nums = [5, 10, 15, 20, 25, 30]

even_no = []
for i in range(len(nums)):
    if nums[i] %2 == 0:
        even_no.append(nums[i])
print(even_no)