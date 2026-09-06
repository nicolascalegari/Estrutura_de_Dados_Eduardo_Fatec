# Exercício 05: Maior Produção em Período de K Dias (Janela Deslisante)

# Uma indústria monitora o total diário de peças fabricadas 
# na lista producao. Implemente a função maior_producao_continua(producao, k) 
# que determine a maior soma de peças produzidas em qualquer sequência 
# contígua de exatamente k dias ( k ≤ len(producao) ).

# Exemplo:

#     Entrada: producao = [100, 200, 150, 400, 300, 100], k = 3
#     Saída: 850 (correspondente ao período [150, 400, 300])

def maior_producao_continua(producao: list[int], k: int) -> int:

    if not producao or k <= 0 or k > len(producao):
        return 0

    # Calcula a soma da primeira janela de tamanho K
    soma_atual = sum(producao[:k])
    maior_soma = soma_atual

    # Desliza a janela pelo restante da lista
    for i in range(k, len(producao)):
        # Adiciona o elemento que entra e remove o que sai
        soma_atual += producao[i] - producao[i - k]

        # Atualiza a maior soma encontrada ate agora
        if soma_atual > maior_soma:
            maior_soma = soma_atual

    return maior_soma

# Tempo = O(N)
# Espaço = O(1)



    
    