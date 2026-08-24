import sys

def resolver():
    #Le todas as entradas de uma vez
    dados = sys.stdin.read().split()
    if not dados:
        return

    iterator = iter(dados)
    num_casos = int(next(iterator))

    for _ in range(num_casos):
        s = next(iterator)
        num_queries = int(next(iterator))

        for _ in range(num_queries):
            r = next(iterator)

            #Validação usando iterator
            iter_s = iter(s)

            #Verifica se todos os caracteres de R estao em S
            if all(char in iter_s for char in r):
                print("Yes")
            else:
                print("No")

if __name__ == "__main__":
    resolver()