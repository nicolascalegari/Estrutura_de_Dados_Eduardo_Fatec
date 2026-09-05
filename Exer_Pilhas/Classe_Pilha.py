
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

# Tempo = O(1)

# Classe sem usar recursos Python

class Pilha_Roots:

    def __ini__(self):
        self.elementos = []
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
