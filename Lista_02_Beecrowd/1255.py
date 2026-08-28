# qtd de testes
n = int(input())

for _ in range(n):
    # le a linha e converte para minusculas
    frase = input().lower()
    
    # Dicionário para armazenar a contagem de cada letra
    frequencias = {}
    
    # Ignora espaços e pontuação
    for caractere in frase:
        if caractere.isalpha():
            if caractere in frequencias:
                frequencias[caractere] += 1
            else:
                frequencias[caractere] = 1
                
    # Acha a maior freq
    maior_frequencia = max(frequencias.values())
    
    # Acha letras que possuem essa maior frequência
    letras_mais_frequentes = []
    for letra, qtd in frequencias.items():
        if qtd == maior_frequencia:
            letras_mais_frequentes.append(letra)
            
    # deixa ordem alfabética
    letras_mais_frequentes.sort()
    
    # Cria um string e printa
    print(''.join(letras_mais_frequentes))
