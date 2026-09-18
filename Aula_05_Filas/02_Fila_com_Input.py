from collections import deque

fila = deque()

for i in range(5):
    nome = input(f"Digite o nome da {i+1}ª pessoa: ")
    fila.append(nome)

print("\nFila:")
print(fila)