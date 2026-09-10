# Le entrada padrao de uma vez so
entrada = open(0).read().split()

if entrada:
    n = int(entrada[0])
    pilha = []
    min_pilha = []
    idx = 1
    saida = []

    for _ in range(n):
        operacao = entrada[idx]

        if operacao == "PUSH":
            valor = int(entrada[idx + 1])
            pilha.append(valor)

            if not min_pilha or valor <= min_pilha[-1]:
                min_pilha.append(valor)
            else:
                min_pilha.append(min_pilha[-1])
            idx += 2

        elif operacao == "POP":
            if not pilha:
                saida.append("EMPTY")
            else:
                pilha.pop()
                min_pilha.pop()
            idx += 1

        elif operacao == "MIN":
            if not pilha:
                saida.append("EMPTY")
            else:
                saida.append(str(min_pilha[-1]))
            idx += 1

    print('\n'.join(saida))