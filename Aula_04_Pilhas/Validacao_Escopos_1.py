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

s = input("Digite a Expressão: ")

p = Pilha()

is_valid = True

for c in s:
    if c == '(' or  c == '{' or c == '[':
        p.push(c)
    else:

        if (c == ')' and p.peek() != '(') or \
           (c == ']' and p.peek() != '[') or \
           (c == '}' and p.peek() != '{'):
            is_valid = False
        else:
            p.pop()

if is_valid and p.is_empty():
    print("Balanciado")
else:
    print("Invalido")