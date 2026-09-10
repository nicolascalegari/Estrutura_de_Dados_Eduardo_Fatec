# Codigo puro e autossuficiente

class Pilha:

    def __init__(self):
        self.elementos = []

    def push(self, item):
        self.elementos.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: pilha vazia")
        return self.elementos.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack underflow: pilha vazia")
        return self.elementos[-1]

    def is_empty(self):
        return len(self.elementos) == 0

    def size(self):
        return len(self.elementos)
    
def avaliar_rpn(tokens: list[str]) -> int:
    pilha = Pilha()
    operadores = {'+', '-', '*', '/'}

    for token in tokens:
        if token not in operadores:
            pilha.push(int(token))
        else:
            b = pilha.pop()
            a = pilha.pop()

            if token == '+':
                pilha.push(a + b)
            elif token == '-':
                pilha.push(a - b)
            elif token == '*':
                pilha.push(a * b)
            elif token == '/':
                pilha.push(int(a / b))

    return pilha.pop()