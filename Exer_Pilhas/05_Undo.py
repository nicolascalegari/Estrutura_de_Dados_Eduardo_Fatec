# Usando recursos Python (Sem criar Classe)

pilha = []

while True:

    acao = input("[D]Desfazer ou [S]Sair: ")

    if acao == 'S':
        break
    elif acao == 'D':

        if len(pilha) > 0:
            ultima = pilha.pop()
        else:
            print("Historico vazio")
    else:
        pilha.append(acao)

    print("Historico: ", pilha)