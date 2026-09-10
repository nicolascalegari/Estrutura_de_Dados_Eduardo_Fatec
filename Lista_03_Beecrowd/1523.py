while True:

    try:

        linha = input()
        if not linha:
            break

        # Carros e Vagas
        n, k = map(int, linha.split())

        if n == 0 and k == 0:
            break

        possivel = True
        estacionamento = []

        for _ in range(n):
            chegada, saida = map(int, input().split())

            if not possivel:
                continue

            # Remove da pilha os carros que ja sairam
            while estacionamento and estacionamento[-1] <= chegada:
                estacionamento.pop()

            # Verifica se o novo carro vai prender o carro da frente
            if estacionamento and saida > estacionamento[-1]:
                possivel = False

            # Verifica se o estacionamento esta lotado
            if len(estacionamento) >= k:
                possivel = False

            # Se correto o carro estaciona
            if possivel:
                estacionamento.append(saida)

        if possivel:
            print("Sim")
        else:
            print("Nao")

    except EOFError:
        break      