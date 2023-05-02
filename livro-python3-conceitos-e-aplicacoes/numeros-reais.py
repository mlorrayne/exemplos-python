print("Início do Programa")
arqreais = open("ValoresReais.txt", "w")
x = float(input("Digite um número real: "))
while x != 0:
    arqreais.write("{0:.3f}\n".format(x))
    x = float(input("Digite um número real: "))
arqreais.close()
print("Fim do Programa")