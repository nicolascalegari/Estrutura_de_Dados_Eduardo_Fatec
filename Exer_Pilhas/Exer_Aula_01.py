# Exercicio feito em aula pelo professor

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

# Tempo = O(1)

pilha = Pilha()

palavra_1 = input()
palavra_2 = ""

for i in palavra_1:
    pilha.push(i)

while not pilha.is_empty():
    palavra_2 += pilha.pop()

print(palavra_1)
print(palavra_2)

