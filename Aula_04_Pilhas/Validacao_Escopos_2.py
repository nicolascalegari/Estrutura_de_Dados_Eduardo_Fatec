class Pilha:

    def __init__(self): self.elementos =[]
    def push(self, item): self.elementos.append(item)
    def pop(self): return self.elementos.pop() if self.elementos else None
    def is_empty(self): return len(self.elementos) == 0

def validar_escopos(s: str) -> bool:
    pilha = Pilha()
    mapa = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in mapa.values():
            pilha.push(char)
        elif char in mapa:
            if pilha.is_empty() or pilha.pop() != mapa[char]:
                return False

    return pilha.is_empty()