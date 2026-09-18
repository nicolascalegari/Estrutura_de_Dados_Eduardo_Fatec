from collections import deque

fila = deque(["Ana", "Bruno", "Carlos"])

print("Fila: ", fila)

fila.append("Daniel") # Inserir elemento no fim da fila

print("Fila: ", fila)

fila.popleft() # Remover primeiro elemento

print("Fila: ", fila)