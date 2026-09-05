historico = []
refazer = []

while True:

    print("1 - Realizar")
    print("2 - Desfazer")
    print("3 - Refazer")
    print("4 - Mostrar")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == '1':
        acao = input("Digite a ação: ")
        historico.append(acao)
        refazer.clear()
        print("Ação realizada: ", acao)

    elif opcao == '2':
        if len(historico) > 0:
            acao = historico.pop()
            refazer.append(acao)
            print("Desfeito: ", acao)
        else:
            print("Nao a acao para desfazer")

    elif opcao == '3':
        if len(refazer) > 0:
            acao = refazer.pop()
            historico.append(acao)
            print("Refeito: ", acao)
        else:
            print("Nao a acao para desfazer")
    
    elif opcao == '4':
        print("Historico: ", historico)
        print("Refazer: ", refazer)
    
    elif opcao == '5':
        print("Saindo...")
        break

    else:
        print("Opcao Invalida")