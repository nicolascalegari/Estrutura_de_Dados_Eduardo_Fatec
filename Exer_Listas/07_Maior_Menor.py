nums = [45,12,78,23,9,56]

# Usando funções do Python
maior = max(nums)
menor = min(nums)

print("Maior:", maior)
print("Menor:", menor)

# Sem usar funções do Python
maior = float('-inf')
menor = float('inf')

for i in range(len(nums)):

    if maior < nums[i]:
        maior = nums[i]
    if menor > nums[i]:
        menor = nums[i]

print("Maior:", maior)
print("Menor:", menor)

