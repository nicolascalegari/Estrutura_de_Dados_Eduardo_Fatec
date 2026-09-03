# Exercício 01: Espelhamento de Elementos (Dois Ponteiros)

# Uma esteira automatizada de produção armazena os códigos 
# das etapas de montagem em uma lista codigos. Implemente a 
# função espelhar_sequencia(codigos) que inverta a ordem de 
# todos os elementos diretamente na lista original (in-place), 
# sem criar uma nova lista e sem utilizar codigos.reverse() ou codigos[::-1].

# Exemplo:

#     Entrada: codigos = [10, 20, 30, 40, 50]
#     Saída: [50, 40, 30, 20, 10]


def espelhar_sequencia(codigos: list) -> list:

    inicio = 0
    fim = len(codigos) - 1

    while inicio < fim:

        codigos[inicio], codigos[fim] = codigos[fim], codigos[inicio]

        inicio += 1
        fim += 1

    return codigos

# Tempo = O(N) (laço executa N/2 interações que é = a N)
# Espaço = O(1) (in place)