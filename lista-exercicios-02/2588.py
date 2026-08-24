import sys

for linha in sys.stdin: # ler todas as linhas
    palavra = linha.strip() # remover quebra de linha
    if not palavra:
        continue
    letras_impares = []
    for letra in palavra:
        if letra in letras_impares:
            letras_impares.remove(letra)
        else:
            letras_impares.append(letra)
            
    # contar quantas letras impar
    total_impares = len(letras_impares)

    if total_impares <= 1:
        print(0)
    else:
        print(total_impares - 1)