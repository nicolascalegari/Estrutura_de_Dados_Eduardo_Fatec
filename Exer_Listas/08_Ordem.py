nums = [8,3,10,1,7,5]

# Usando função python
nums.sort()

print(nums)

nums.sort(reverse=True)

print(nums)

nums = [8,3,10,1,7,5]

n = len(nums)

for i in range(n):
    for j in range(n - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print("Crescente:", nums)

nums = [8,3,10,1,7,5]

n = len(nums)

for i in range(n):
    for j in range(n - i - 1):
        if nums[j] < nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print("Decrescente:", nums)

