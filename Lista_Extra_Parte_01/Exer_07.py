# Exercício 07: Período Mínimo para Atingir Meta Financeira (Janela Dinamica)

# Um comerciante registrou os ganhos diários em uma lista de números 
# inteiros positivos vendas. Implemente a função menor_periodo_meta(vendas, meta) 
# que retorne o menor número de dias consecutivos necessários para somar um valor 
# maior ou igual a meta. Se a meta não puder ser atingida, retorne 0.

# Exemplos:

#     Entrada: vendas = [2, 1, 5, 2, 3, 2], meta = 7 ⟶ Saída: 2 (período [5, 2])
#     Entrada: vendas = [1, 2, 1], meta = 10 ⟶ Saída: 0

def menor_periodo_meta(vendas: list[int], meta: int) -> int:

    inicio = 0
    soma_atual = 0

    # Inicia com o valor maior possivel
    menor_comprimento = float('inf')

    # O ponteiro fim expande a janela para a direita
    for fim in range(len(vendas)):
        soma_atual += vendas[fim]

        # Enquanto a meta for atingida, tenta diminuir a janela pela equerda
        while soma_atual >= meta:
            comprimento_atual = fim - inicio + 1
            if comprimento_atual < menor_comprimento:
                menor_comprimento = comprimento_atual

            soma_atual -= vendas[inicio]
            inicio += 1

    # Se menor_comprimento continuar infinito, significa que a meta nunca foi atingida
    return menor_comprimento if menor_comprimento != float('inf') else 0

# Tempo = O(N)
# Espaço = O(1)
