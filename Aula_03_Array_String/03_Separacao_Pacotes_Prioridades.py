# Exercício 03: Separação de Pacotes por Prioridade (Dois Ponteiros)

# Em um centro de distribuição, pacotes com peso par 
# têm prioridade padrão e pacotes com peso ímpar têm 
# prioridade urgente. Implemente a função separar_por_prioridade(pesos) 
# que reorganize a lista de modo que todos os números pares fiquem no 
# início e todos os ímpares fiquem no final (in-place). A ordem interna 
# entre os números pares ou ímpares não precisa ser preservada.

# Exemplo:

#     Entrada: pesos = [7, 2, 9, 4, 6, 1]
#     Saída Possível: [6, 2, 4, 9, 7, 1] (qualquer configuração com pares no início e ímpares no final)

def separar_por_prioridade(pesos: list[int]) -> list[int]:

    inicio = 0
    fim = len(pesos) - 1

    while inicio < fim:

        if pesos[inicio] % 2 == 0:
            inicio += 1
        elif pesos[fim] % 2 != 0:
            fim -= 1
        else:
            pesos[inicio], pesos[fim] = pesos[fim], pesos[inicio]
            inicio += 1
            fim -= 1
    
    return pesos

# Tempo = O(N)
# Espaço = O(1) (in place)