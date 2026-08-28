n = int(input())
for i in range(n):
    anos_entrada = int(input())
    ano_saida = 2015 - anos_entrada
    if ano_saida > 0:
        print(f"{ano_saida} D.C.")
    else:
        ano_negativo = 1 - ano_saida
        print(f"{ano_negativo} A.C.")