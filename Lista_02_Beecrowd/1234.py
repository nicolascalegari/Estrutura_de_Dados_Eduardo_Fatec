import sys

# o sys.stdin le o arquivo de entrada inteiro
for linha in sys.stdin:
    # remover as quebras de linha
    frase = linha.rstrip('\r\n')
    # break se a linha ficar vazia apos o arquivo acabar
    if not linha:
        break

    resultado = ""
    deve_ser_maiuscula = True

    for caractere in frase:
        if caractere == " ":
            resultado += caractere
        else:
            if deve_ser_maiuscula == True:
                resultado += caractere.upper()
                deve_ser_maiuscula = False
            else:
                resultado += caractere.lower()
                deve_ser_maiuscula = True
    print(resultado)
