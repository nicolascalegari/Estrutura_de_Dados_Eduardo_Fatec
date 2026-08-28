# Muitos problemas do Beecrowd pedem múltiplos valores em uma única linha de entrada, 
# separados por espaço.

linha = input() # "3 7 10"
partes = linha.split() # quebra a string em uma lista de strings, usando espaço
print(partes)

# .split() gera strings, mas geralmente precisa-se de numeros

a, b, c = map(int, input().split())
print(a + b + c)

# input().split() -> lista de strings: ['3','7','10']
# map(int, ...) -> converte cada item para int
# Podemos desempacotar direto em variaveis (a, b, c)

numeros = list(map(int, input().split()))
print(numeros) #[3, 7, 10]