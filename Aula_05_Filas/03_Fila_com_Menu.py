from collections import deque

fila = deque()

while True:
    print("\n---MENU---")
    print("1 - Adicionar pessoa")
    print("2 - Atender pessoa")
    print("3 - Mostrar fila")
    print("4 - Sair")

    opcao = int(input("Escolha um opcao: "))

    if opcao == 1:
        nome = input("Digite o nome: ")
        fila.append(nome)
        print(f"{nome} entrou na fila.")

    elif opcao == 2:
        if fila:
            pessoa = fila.popleft()
            print(f"Atendendo {pessoa}.")
        else:
            print("Fila vazia!")

    elif opcao == 3:
        if fila:
            print("Fila:", list(fila))
        else:
            print("Fila vazia!")

    elif opcao == 4:
        print("Programa encerrado!")
        break

    else:
        print("Opcao inválida.")