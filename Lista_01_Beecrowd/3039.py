n = int(input())
carrinho = 0
boneca = 0
for i in range(n):
    nome, sexo = input().split()
    if sexo == 'M':
        carrinho += 1
    else:
        boneca += 1
print(f"{carrinho} carrinhos\n{boneca} bonecas")
