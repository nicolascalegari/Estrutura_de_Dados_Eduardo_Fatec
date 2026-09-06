# listas guardam varias informacoes em um unica variavel

numeros = [4,7,2,9,1]
nomes = ["ana", "bruno", "carla"]
mista = [1, "dois", 3.0, True]
frutas = ["maca", "banana", "uva"]

vazia = []

# Podem conter qualquer tipo de dados
# Sao mutaveis

print(numeros)
print(nomes)
print(mista)

# Acessando por indice

print(frutas[0])
print(frutas[1])
print(frutas[-1]) # indice negativo = a partir do fim

# Substituicao de valor dentro da lista
frutas[1] = "morango"
print(frutas)

# funcao .append() adiciona ao final da lista
frutas = ["maca", "banana"]
frutas.append("uva") # adiciona uva ao final da lista
print(frutas)

# usado dentro de laços para montar uma lista
quadrados = []
for i in range(5):
    quadrados.append(i ** 2) # i potencia de 2
print(quadrados) # [0,1,4,9,16]

# percorrer lista com for:
frutas = ["maca", "banana", "uva"]
for fruta in frutas:
    print(fruta)

# ou usando len() mais range():
# len(frutas) retorna o tamanho da lista (qtd de itens)
for i in range(len(frutas)):
    print(i, frutas[i])
