while True:

    N = int(input())
    if N == 0:
        break

    while True:
        linha = input().split()

        if linha == ['0']:
            print()
            break

        desejado = [int(x) for x in linha]
        estacao = []
        pont_saida = 0

        for vagao in range(1, N + 1):
            estacao.append(vagao)

            while estacao and estacao[-1] == desejado[pont_saida]:
                estacao.pop()
                pont_saida += 1

        if len(estacao) == 0:
            print("Yes")
        else:
            print("No")