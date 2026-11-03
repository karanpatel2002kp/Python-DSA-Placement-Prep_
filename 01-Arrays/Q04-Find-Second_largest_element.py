# Find Second Largest Number solve karte hain.
# Problem:
# nums = [12, 45, 7, 89, 23]
# Expected output:
# 45

nums = [12,45,7,89,23]
largest = nums[0]
second_largest = None

for value in nums:
    if value>largest:
        second_largest = largest
        largest = value

    elif value<largest and value>second_largest:
        second_largest = value

print(second_largest)
        