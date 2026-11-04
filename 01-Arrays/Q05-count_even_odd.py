# nums = [12, 5, 8, 7, 10, 3, 15, 20]
# Expected output:
# Even numbers: 4
# Odd numbers: 4

nums = [12, 5, 8, 7, 10, 3, 15, 20]
even_count = 0
odd_count = 0
for i in range(len(nums)):
    if nums[i]%2==0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("Even numbers:",even_count)
print("odd numbers", odd_count)
        