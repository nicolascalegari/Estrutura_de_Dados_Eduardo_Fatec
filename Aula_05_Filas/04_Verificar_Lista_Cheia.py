from collections import deque

fila = deque()

limite = 5

for i in range(7):
    nome = input("Digite o nome: ")

    if len(fila) < limite:
        fila.append(nome)
        print(f"{nome} entrou na fila.")
    else:
        print("Fila cheia!")

print("\nFila final: ")
print(list(fila))