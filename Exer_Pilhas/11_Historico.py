historico = []

while True:

    print("1 = Visitar pagina")
    print("2 = Voltar")
    print("3 = Atual")
    print("4 = Historico")
    print("5 = Sair")

    opcao = int(input())

    if opcao == 1:
        pagina = input("Site: ")
        historico.append(pagina)
        print("Visitando:", pagina)

    elif opcao == 2:
        if len(historico) > 1:
            pagina = historico.pop()
            print("Voltando de:", pagina)
        else:
            print("Nao tem para onde voltar")

    elif opcao == 3:
        if len(historico) > 0:
            print("Pagina atual:", historico[-1]) #Pega o elemento do topo da pilha
        else:
            print("Nenhuma pagina aberta")

    elif opcao == 4:
        print("Historico:")
        print(historico)

    elif opcao == 5:
        break

    else:
        print("Opcao invalida")