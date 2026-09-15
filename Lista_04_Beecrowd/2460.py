n = int(input())

#fila inicial
fila = input().split()

m = int(input())

# Le quem saiu em um conjunto (set)
sairam = set(input().split())

# Cria a fila final apenas com quem nao esta no conjunto de quem saiu
fila_final = [pessoa for pessoa in fila if pessoa not in sairam]

print(" ".join(fila_final))