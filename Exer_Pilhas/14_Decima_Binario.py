numero = int(input("Digite um decimal: "))

if numero == 0:
    print("Binario: 0")

else:

    pilha = []

    while numero > 0:

        resto = numero % 2

        pilha.append(resto)

        numero = numero // 2

    binario = ""

    while len(pilha) > 0:

        binario += str(pilha.pop())

    print("Binario: ", binario)