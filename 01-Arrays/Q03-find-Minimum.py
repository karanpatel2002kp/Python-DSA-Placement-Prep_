arr = [12, 5, 30, 2, 18]
mininum = arr[0]

for i in range(len(arr)):
    if arr[i]<mininum:
        mininum = arr[i]
print("minimum number:",mininum)