# Exercício 02: Filtragem de Leituras Inválidas (Um Ponteiro)

# Um sensor de temperatura registra medições em uma lista leituras. 
# O valor -1 indica uma falha momentânea de leitura. Implemente a função 
# reorganizar_falhas(leituras) que mova todas as leituras de valor -1 para o 
# final da lista, preservando a ordem original de todas as leituras válidas. 
# A alteração deve ser feita in-place.

# Exemplo:

#     Entrada: leituras = [22, -1, 25, -1, 30, 28]
#     Saída: [22, 25, 30, 28, -1, -1]

def reorganizar_falhas(leituras: list[int]) -> list[int]:

    ponteiro = 0

    # Mover leituras validas para frente
    for i in range(len(leituras)):

        if leituras[i] != -1:
            leituras[ponteiro] = leituras[i]
            ponteiro += 1

    # Preenche o restante da lista
    while ponteiro < len(leituras):
        leituras[ponteiro] = -1
        ponteiro += 1
    
    return leituras

# Tempo = O(N)
# Espaço = O(1) (in place)