n = int(input())

for i in range(n):
    linha = input()

    # encontra o meio da string
    meio = len(linha) // 2

    # separa a primeira e segunda metade - fatiamento
    primeira_metade = linha[0:meio]
    segunda_metade = linha[meio:]

    # inverte a primeira e a segunda usando [::-1]
    primeira_invertida = primeira_metade[::-1]
    segunda_invertida = segunda_metade[::-1]

    # juntar as partes
    linha_correta = primeira_invertida + segunda_invertida

    print(linha_correta)