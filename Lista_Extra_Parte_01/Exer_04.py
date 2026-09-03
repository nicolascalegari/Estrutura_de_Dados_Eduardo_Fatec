# Exercício 04: Verificação de Simetria em Sequências (Dois Ponteiros)

# Um sistema de auditoria precisa verificar se uma sequência 
# de números inteiros nums é perfeitamente simétrica (possui os 
# mesmos valores lidos da esquerda para a direita e da direita 
# para a esquerda). Implemente a função verificar_simetria(nums) que 
# retorne True se for simétrica e False caso contrário, sem criar uma 
# lista invertida auxiliar.

# Exemplos:

#     Entrada: nums = [1, 4, 9, 4, 1] ⟶ Saída: True
#     Entrada: nums = [1, 2, 3, 4] ⟶ Saída: False

def verificar_simetria(nums: list[int]) -> bool:

    inicio = 0
    fim = len(nums) - 1

    # Compara os elementos das pontas em direção ao centro
    while inicio < fim:

        if nums[inicio] != nums[fim]:
            # Encontrou assimetria
            return False

        inicio += 1
        fim -= 1

    #Se chegou aqui, não teve assimetria (palindromo)
    return True

# Tempo = O(N)
# Espaço = O(1)