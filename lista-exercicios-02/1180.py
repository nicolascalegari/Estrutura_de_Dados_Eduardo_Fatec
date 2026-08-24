# Le o tamanho do vetor
n = int(input())

# Le a linha com os numeros em um lista
vetor = list(map(int, input().split()))

# Achar o menor e indice
menor = min(vetor)
posicao = vetor.index(menor)

print(f"Menor valor: {menor}")
print(f"Posicao: {posicao}")