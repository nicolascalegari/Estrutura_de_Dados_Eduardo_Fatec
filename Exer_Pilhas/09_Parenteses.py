parenteses = input("Digite uma expressão: ")

pilha = []

valida = True

for c in parenteses:

    if c == '(':
        pilha.append(c)

    elif c == ')':
        if len(pilha) == 0:
            valida = False
            break

        pilha.pop()

if len(pilha) != 0:
    valida = False

if valida:
    print("Valido")
else:
    print("Invalido")