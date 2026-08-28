# Quando usar For ou While?

# Sei o numero de repeticoes (range) -> FOR
# Rpeticao ate que um condicao deixar de ser verdadeira -> (WHILE)

resposta = ""
while resposta != "sair":
    resposta = input("Digite algo (ou 'sair'): ")

for tentativa in range(3):
    print("Tentativa numero", tentativa + 1)
    