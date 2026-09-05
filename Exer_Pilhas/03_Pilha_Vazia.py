# Usando recursos Python (Sem criar Classe)

def pilha_vazia(pilha):
    return len(pilha) == 0

pilha = []

if pilha_vazia(pilha):
    print("A pilha esta vazia")
else:
    print("A pilha nao esta vazia")

pilha.append(10)

if pilha_vazia(pilha):
    print("A pilha esta vazia")
else:
    print("A pilha nao esta vazia")