n = int(input())

for _ in range(n):

    linha = input()

    diamantes = 0
    menores_abertos = 0

    for char in linha:

        if char == '<':

            menores_abertos += 1

        elif char == '>':

            if menores_abertos > 0:

                diamantes += 1
                menores_abertos -= 1

    print(diamantes)