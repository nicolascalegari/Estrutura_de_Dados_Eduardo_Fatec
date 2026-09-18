from collections import deque

texto = input("Digite uma palavra: ")

# Remove os espaços e transforma tudo em minusculo
texto = texto.replace(" ", "").lower()

fila = deque(texto)

palindromo = True

while len(fila) > 1:
    primeiro = fila.popleft()
    ultimo = fila.pop()

    if primeiro != ultimo:
        palindromo = False
        break

if palindromo:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")