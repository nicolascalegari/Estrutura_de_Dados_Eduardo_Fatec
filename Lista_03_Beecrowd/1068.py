while True:

    try:

        expressao = input().strip()
        pilha = []
        correto = True

        for char in expressao:
            if char == '(':
                pilha.append('(')
            elif char == ')':
                if len(pilha) == 0:
                    correto = False
                    break
                else:
                    pilha.pop()

        if correto and len(pilha) == 0:
            print("correct")
        else:
            print("incorrect")

    except EOFError:
        break
