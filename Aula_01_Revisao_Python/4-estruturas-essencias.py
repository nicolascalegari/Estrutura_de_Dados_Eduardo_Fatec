# Lista [] -> ordenada, mutavel, repeticao
# Tupla () -> ordenada, imutavel, repeticao
# Dicionais {chave: valor} -> ordenada, mutavel, chaves nao repetem
# Set set() -> desordenada, mutavel, sem repeticao

# Listas: A base de quase tudo
numeros = [4,7,2,9,1]

# Tuplas: Mais rapidas e seguras para leitura
ponto = (10,20) 
cores = ("vermelho", "verde", "azul")

# Dicionarios: acesso rapido por chave
aluno = {
    "nome": "Nicolas",
    "idade": 37,
    "curso": "ADS"
}
print(aluno["nome"])
aluno["idade"] = 38 # modifica o valor
print(aluno["idade"])