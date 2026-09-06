# Exercício 09: Ponto de Equilíbrio de Cargas

# Uma balança digital precisa identificar o primeiro índice 
# de equilíbrio em uma sequência de cargas cargas. O índice 
# de equilíbrio i ocorre quando a soma dos pesos estritamente à 
# esquerda de i é igual à soma dos pesos estritamente à direita de i. 
# Implemente a função encontrar_ponto_equilibrio(cargas). Se não houver equilíbrio, 
# retorne -1.

# Exemplos:

#     Entrada: cargas = [2, 4, 6, 1, 5] ⟶ Saída: 2
#     (Esquerda: $2+4 = 6$; Direita: $1+5 = 6$)
#     Entrada: cargas = [1, 2, 3] ⟶ Saída: -1

def encontrar_ponto_equilibrio(cargas: list[int]) -> int:

    soma_total = sum(cargas)
    soma_esquerda = 0

    for i in range(len(cargas)):
        # A soma à direita é o total menos o que está à esquerda e menos o elemento atual
        soma_direita = soma_total - soma_esquerda - cargas[i]

        # Verifica se encontramos o ponto de equilíbrio
        if soma_esquerda == soma_direita:
            return i

        # Atualiza a soma à esquerda para a próxima iteração
        soma_esquerda += cargas[i]

    return -1

# Tempo = O(N)
# Espaço = O(1)