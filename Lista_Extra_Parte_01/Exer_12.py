# Exercício 12: Maior Sequência Contínua de Dias Positivos

# Um investidor registrou os rendimentos diários na lista rendimentos. 
# Implemente a função maior_sequencia_positiva(rendimentos) que encontre 
# o comprimento da maior sequência contínua de dias com rendimento positivo ( > 0 ).

# Exemplo:

#     Entrada: rendimentos = [10, 20, -5, 30, 40, 50, 60, -2, 10]
#     Saída: 4 (sequência [30, 40, 50, 60])

def maior_sequencia_positiva(rendimentos: list[int]) -> int:

    max_seq = 0
    seq_atual = 0

    for rendimento in rendimentos:
        if rendimento > 0:
            # Incrementa a sequência atual se o rendimento for positivo
            seq_atual += 1

            # Atualiza o máximo global encontrado até agora
            if seq_atual > max_seq:
                max_seq = seq_atual
        else:
            # Quebra a sequência contínua se o rendimento for <= 0
            seq_atual = 0

    return max_seq

# Tempo = O(N)
# Espaço = O(1)