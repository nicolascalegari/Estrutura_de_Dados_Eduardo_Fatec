N = []

#Ler os 20 valores
for i in range(20):
    N.append(int(input()))

#Inversao do vetor
for i in range(10):
    N[i], N[19 - i] = N[19 - i], N[i]

#Impressao
for i in range(20):
    print(f"N[{i}] = {N[i]}")