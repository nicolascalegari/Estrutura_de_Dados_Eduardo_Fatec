X = int(input())
Y = int(input())
soma = 0
if X > Y:
    X, Y = Y, X
for numero in range(X + 1, Y):
    if numero % 2 != 0:
        soma += numero
print(soma)