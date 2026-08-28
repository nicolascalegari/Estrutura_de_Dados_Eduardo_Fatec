risada = input()

#Filtra apenas as vogais
vogais = [char for char in risada if char in 'aeiou']

#Inverte a lista de vogais para comparar usando Fatiamente
vogais_invertidas = vogais[::-1]

#Verifica se a sequencia é a mesma nos dois sentidos
if vogais == vogais_invertidas:
    print('S')
else:
    print('N')