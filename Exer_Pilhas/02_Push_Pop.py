class Pilha_Roots:

    def __init__(self):
        self.elementos = [None] * 100
        self.topo = - 1

    def push(self, item):
        self.topo = self.topo + 1
        self.elementos[self.topo] = item

    def pop(self):
        if self.topo == -1:
            print("Pilha Vazia")
            return None

        item = self.elementos[self.topo]
        self.elementos[self.topo] = None
        self.topo = self.topo - 1

        return item

    def is_empty(self):
        if self.topo == -1:
            print("Pilha Vazia")
            return True
        else:
            return False
        
    def see_topo(self):
        if self.topo == -1:
            print("Pilha Vazia")
            return None

        return self.elementos[self.topo]

    def see(self):
        if self.topo == -1:
            print("Pilha Vazia")
            return None  

        print("Pilha: ")
        i = self.topo
        while i >= 0:
            print(self.elementos[i])
            i -= 1  

# --------------------------------------------

pilha = Pilha_Roots()

pilha.push(100)
pilha.push(200)
pilha.push(300)
pilha.push(400)
pilha.push(500)

print(pilha.see_topo())

print(pilha.see())

pilha.pop()
print(pilha.see_topo())
pilha.pop()
print(pilha.see_topo())

print(pilha.see())