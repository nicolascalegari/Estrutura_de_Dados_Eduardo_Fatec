class Pilha:

    def __init__(self):
        self.elementos = []

    def push(self, item):
        self.elementos.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pilha esta Vazia")
        return self.elementos.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Pilha esta Vazia")
        return self.elementos[-1]

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.elementos)

    def see(self):
        return list(self.elementos)

 #----------------------------------   

historico = Pilha()

while True:

    opcao = input("[A]ção, [D]esfazer, [S]air: ")

    if opcao == 'A':
        acao = input("Digite a ação: ")
        historico.push(acao)
        print(historico.see())
    elif opcao == 'D':
        if historico.is_empty():
            print("Historico Vazio")
        else:
            acao = historico.pop()
            print(historico.see())
    elif opcao == 'S':
        break
    else:
        print("Opcao Invalida")

