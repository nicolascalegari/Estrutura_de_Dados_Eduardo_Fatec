# Exercício 10: Comparador de Inventário de Letras (Contagem de Frequencia)

# Em um jogo de formação de palavras, o sistema recebe duas 
# palavras palavra1 e palavra2 compostas apenas por letras minúsculas ('a' até 'z'). 
# Implemente a função mesmo_inventario(palavra1, palavra2) que retorne True se 
# ambas possuírem exatamente as mesmas letras nas mesmas quantidades, 
# sem utilizar ordenação (sorted()).

# Exemplos:

#     Entrada: palavra1 = "alegria", palavra2 = "galeria" ⟶ Saída: True
#     Entrada: palavra1 = "teste", palavra2 = "texto" ⟶ Saída: False

def mesmo_inventario(palavra1: str, palavra2: str) -> bool:
    # Se os tamanhos forem diferentes, o inventário não pode ser igual
    if len(palavra1) != len(palavra1):
        return False

    contagem_letras = {} # Dicionario

    # Registra a frequência de cada letra da palavra1
    for letra in palavra1:
        contagem_letras[letra] = contagem_letras.get(letra, 0) + 1

    # Deduz as letras com base na palavra2
    for letra in palavra2:
        # Se a letra não existir ou sua contagem já for zero, os inventários diferem
        if letra not in contagem_letras or contagem_letras[letra] == 0:
             return False
        contagem_letras[letra] -= 1

    return True

# Tempo = O(N)
# Espaço = O(1)