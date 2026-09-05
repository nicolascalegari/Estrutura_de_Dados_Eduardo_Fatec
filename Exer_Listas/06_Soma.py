nums = [5,10,15,20,25]

soma = sum(nums) # Função interna no Python que soma

print(soma)

i = 0
soma = 0

while i < len(nums):
    soma += nums[i]
    i += 1
print(soma)

i = 0
soma = 0

for n in nums:
    soma += n
print(soma)
