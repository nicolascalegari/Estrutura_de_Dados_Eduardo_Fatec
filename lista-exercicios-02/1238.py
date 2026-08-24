# Encerra antes de dar RunTime Error
try:
    n = int(input())

    for _ in range(n):
        palavra1, palavra2 = input().split()

        resultado = "" # string vazia
        menor_tamanho = min(len(palavra1), len(palavra2))

        for i in range(menor_tamanho):
            resultado += palavra1[i] + palavra2[i]

        resultado += palavra1[menor_tamanho:] + palavra2[menor_tamanho:]

        print(resultado)

except Exception:
    pass