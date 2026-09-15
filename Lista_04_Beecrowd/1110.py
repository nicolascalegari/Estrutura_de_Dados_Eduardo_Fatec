while True:
    n = int(input())
    if n == 0:
        break

    cartas = list(range(1, n + 1))
    descartadas = []

    while len(cartas) > 1:
        topo = cartas.pop(0)
        descartadas.append(str(topo))

        proxima = cartas.pop(0)
        cartas.append(proxima)

    print(f"Discarded cards: {', '.join(descartadas)}")
    print(f"Remaining card: {cartas[0]}")