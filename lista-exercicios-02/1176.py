# lista com os dois primeiros valores
fibonacci = [0, 1]

# calcular do termo 2 ao 60
for i in range(2, 61):
    proximo_numero = fibonacci[i - 1] + fibonacci[i - 2]
    # add novo nuemro ao final da lista
    fibonacci.append(proximo_numero)

# Qtd de testes
T = int(input())

for caso in range(T):
    # le o termo fibonacci
    N = int(input())
    # busca o valor na lista posicao N
    valor_fib = fibonacci[N]
    print(f"Fib({N}) = {valor_fib}")