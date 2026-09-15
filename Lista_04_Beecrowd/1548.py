n = int(input())

for _ in range(n):
    m = int(input())

    fila_original = list(map(int, input().split()))

    fila_ordenada = sorted(fila_original, reverse=True)

    nao_mudaram = 0

    for i in range(m):
        if fila_original[i] == fila_ordenada[i]:
            nao_mudaram += 1

    print(nao_mudaram)