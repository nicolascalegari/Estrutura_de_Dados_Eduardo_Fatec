n = int(input())

pilha = ['F', 'A', 'C', 'E']
brindes = 0

for _ in range(n):
    # Se a piçlha esvaziar, reinicia com FACE
    if not pilha:
        pilha = ['F', 'A', 'C', 'E']

    # Ler as 4 letras digitadas
    letras = input().split()

    topo = pilha[-4:]

    # Inverte as 4 letras do topo
    topo_inv = [topo[3], topo[2], topo[1], topo[0]]

    # Compara entrada com topo invertido
    if letras == topo_inv:
        brindes += 1
        del pilha[-4:]
    else:
        # Se nao for igual add as 4 letras na pilha
        pilha.extend(letras)

print(brindes)