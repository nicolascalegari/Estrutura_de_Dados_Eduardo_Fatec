# Usando recursos Python (Sem criar Classe)

p = input("Palavra: ")

pilha = []

for l in p:
    pilha.append(l)

p_i = ""

while len(pilha) > 0:
    p_i += pilha.pop()

print(p)
print(p_i)