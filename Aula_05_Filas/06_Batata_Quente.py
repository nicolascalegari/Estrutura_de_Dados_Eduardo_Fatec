from collections import deque

fila = deque()

quantidade = int(input("Quantidade de jogadores: "))

# Adiciona os jogadores a fila:
for i in range(quantidade):
    nome = input(f"Nome do jogador {i + 1}: ")
    fila.append(nome)

passes = int(input("Quatidade de passes: "))

print("\n---JOGO BATATA QUENTE---")

while len(fila) > 1:
    # Passa a batata
    for i in range(passes - 1):
        jogador = fila.popleft()
        fila.append(jogador)

    # Jogador que ficou com a batata é eliminado
    eliminado = fila.popleft()

    print(f"{eliminado} foi elimado.")

print("\nVencedor:", fila[0])