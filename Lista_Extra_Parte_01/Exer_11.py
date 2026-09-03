# Exercício 11: Compactação de Sequências Repetidas (Dois Ponteiros)

# Implemente a função remover_duplicados_consecutivos(numeros) 
# que receba uma lista de números inteiros onde repetições 
# consecutivas podem ocorrer e reorganize a lista in-place de 
# modo que cada número apareça apenas uma vez no início. 
# A função deve retornar o novo tamanho da lista sem repetições consecutivas.

# Exemplo:

#     Entrada: numeros = [1, 1, 2, 3, 3, 4]
#     Saída: Retorna 4, com a lista modificada contendo [1, 2, 3, 4, ...]

def remover_duplicados_consecutivos(numeros: list[int]) -> int:
    # Se a lista estiver vazia, o novo tamanho é 0
    if not numeros:
        return 0

    # O ponteiro 'lento' marca a posição do último elemento único encontrado
    lento = 0

    # O ponteiro 'rapido' percorre toda a lista a partir do segundo elemento
    for rapido in range(1, len(numeros)):
        # Se o elemento atual for diferente do último elemento único salvo
        if numeros[rapido] != numeros[lento]:
            lento += 1
            numeros[lento] = numeros[rapido]

    # O novo tamanho será o índice 'lento' + 1
    return lento + 1

# Tempo O(N)
# Espaço O(1)
