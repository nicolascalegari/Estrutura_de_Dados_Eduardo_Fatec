while True:
    n = int(input())
    if n == 0:
        break

    h = list(map(int, input().split()))
    picos = 0

    for i in range(n):
        anterior = h[i - 1]
        atual = h[i]

        if i == n - 1:
            proximo = h[0]
        else:
            proximo = h[i + 1]

        if (atual > anterior and atual > proximo) or (atual < anterior and atual < proximo):
            picos += 1

    print(picos)