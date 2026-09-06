# Percorrendo dicionarios

aluno = {"nome": "Nicolas", "idade": 37}

for chave in aluno:
    print(chave, "->", aluno[chave])

for chave, valor in aluno.items():
    print(chave, "->", valor)

for valor in aluno.values():
    print(valor)

# .keys() -> so as chaves
# .values() -> so os valores
# .items() -> pares (chaves, valor)