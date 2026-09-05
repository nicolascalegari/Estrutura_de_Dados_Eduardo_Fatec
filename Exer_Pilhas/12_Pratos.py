pilha = []

while True:

    print("1 - Add Prato")
    print("2 - Retirar")
    print("3 - Ver Topo")
    print("4 - Mostrar")
    print("5 - Sair")

    op = int(input())

    if op == 1:
        prato = input("Digite o item a ser empilhado: ")
        pilha.append(prato)

    elif op == 2:
        if len(pilha) > 0:
            prato = pilha.pop()
            print(f"{prato}, desempilhado.")
        else:
            print("Pilha Vazia!")

    elif op == 3:
        if len(pilha) > 0:
            print(f"Topo: {pilha[-1]}")
        else:
            print("Pilha Vazia!")

    elif op == 4:
        print("Pilha: ", pilha)

    elif op == 5:
        break

    else:
        print("Op. Invalida")
