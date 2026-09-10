t = int(input())

pares = {')': '(', ']': '[', '}': '{'}

for _ in range(t):

    expressao = input().strip()
    pilha = []
    valido = True

    for char in expressao:

        if char in "([{":
            pilha.append(char)
        elif char in ")]}":
            if not pilha or pilha[-1] != pares[char]:
                valido = False
                break
            else:
                pilha.pop()

    if valido and not pilha:
        print('S')
    else:
        print('N')