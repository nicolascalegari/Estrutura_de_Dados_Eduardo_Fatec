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