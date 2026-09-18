tam = 5

fila = [None] * tam
inicio = 0
fim = 0
quantidade = 0

def adicionar():
    global fim, quantidade

    if quantidade == tam:
        print("\nFila Cheia!")
        return

    nome = input("Nome: ")

    fila[fim] = nome
    fim = (fim + 1) % tam
    quantidade += 1

    print("Pessoa adicionada!")

def atender():
    global inicio, quantidade

    if quantidade == 0:
        print("\nFila Vazia!")
        return

    print(f"\nAtendendo: {fila[inicio]}")

    fila[inicio] = None
    inicio = (inicio + 1) % tam
    quantidade -= 1

def mostrar():
    if quantidade == 0:
        print("\nFila vazia!")
        return

    print("\nFila: ")

    for i in range(quantidade):
        posicao = (inicio + i) % tam
        print(f"[{fila[posicao]}]", end="")

        if i < quantidade - 1:
            print(" -> ", end="")

    print()

while True:
    print("\n---FILA DE ATENDIMENTO---")
    print("1 - Adicionar pessoa")
    print("2 - Atender pessoa")
    print("3 - Mostrar fila")
    print("4 - Sair")

    opcao = int(input("Escolha: "))

    if opcao == 1:
        adicionar()
    elif opcao == 2:
        atender()
    elif opcao == 3:
        mostrar()
    elif opcao == 4:
        print("\nPrograma encerrado!")
        break
    else:
        print("\nOpcao inválida!")