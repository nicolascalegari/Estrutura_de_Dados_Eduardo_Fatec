expressao = input("Digite a expressao: ")

pilha = []

elementos = expressao.split()

for char in elementos:

    if char.isdigit():

        pilha.append(int(char))

    else: 

        num_2 = pilha.pop()
        num_1 = pilha.pop()

        if char == '+':
            resul = num_1 + num_2

        if char == '-':
            resul = num_1 - num_2

        if char == '*':
            resul = num_1 * num_2

        if char == '/':
            if num_2 != 0:
                resul = num_1 / num_2
            else:
                resul = "Erro!"
                pilha.append(resul)

print("Resultado: ", resul)