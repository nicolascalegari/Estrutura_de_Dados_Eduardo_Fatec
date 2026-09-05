expressao = input("Digite a expressao: ")

pilha = []

pares = {')': '(', ']': '[', '}': '{'}

valida = True

for c in expressao:
    if c in '([{':
        pilha.append(c)
    elif c in ')]}':
        if len(pilha) == 0:
            valida = False
            break

        topo = pilha.pop()

        if topo != pares[c]:
            valida = False
            break

if len(pilha) != 0:
    valida = False

if valida:
    print("Valida")
else:
    print("Invalida")