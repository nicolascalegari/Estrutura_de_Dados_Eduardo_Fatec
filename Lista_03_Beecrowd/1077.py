def prioridade(operador):
    if operador == '+' or operador == '-':
        return 1
    if operador == '*' or operador == '/':
        return 2
    if operador == '^':
        return 3
    return 0

n = int(input())

for _ in range(n):
    expressao = input()
    resultado = []
    pilha = []
    
    for caractere in expressao:
        if caractere.isalnum():
            resultado.append(caractere)
            
        elif caractere == '(':
            pilha.append(caractere)
            
        elif caractere == ')':
            while pilha and pilha[-1] != '(':
                resultado.append(pilha.pop())
            if pilha:
                pilha.pop()
                
        else:
            while pilha and prioridade(pilha[-1]) >= prioridade(caractere):
                resultado.append(pilha.pop())
            pilha.append(caractere)
            
    while pilha:
        resultado.append(pilha.pop())
        
    print("".join(resultado))
