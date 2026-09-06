# Pilha Encadeada (Node-Based)

class Node:

    def __init__(self, dado, proximo=None):
        self.dado = dado
        self.proximo = proximo

class PilhaEncadeada:

    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def push(self, item):
        self.topo = Node(item, proximo=self.topo)
        self.tamanho += 1

    def pop(self):
        if not self.topo:
            raise IndexError("Pilha Vazia")
        item = self.topo.dado
        self.topo = self.topo.proximo
        self.tamanho -= 1
        return item