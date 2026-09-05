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

p = input()

pilha = Pilha()

i = 0

for c in p:
    i += 1

j = 0

while j < i:
    pilha.push(p[j])
    j += 1

p_i = ""

while not pilha.is_empty():
    p_i += pilha.pop()

print(p)
print(p_i)