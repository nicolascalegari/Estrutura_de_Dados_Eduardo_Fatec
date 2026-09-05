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

    #---------------------------------------

nomes = Pilha()

nomes.push("nicolas")
nomes.push("alexandre")
nomes.push("calegari")

if nomes.is_empty():
    print("Esta Vazia")
else:
    print("Nao esta Vazia")

nomes.pop()
nomes.pop()
nomes.pop()

if nomes.is_empty():
    print("Esta Vazia")
else:
    print("Nao esta Vazia")



