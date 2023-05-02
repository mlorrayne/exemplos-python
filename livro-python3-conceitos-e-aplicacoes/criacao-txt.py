print("Início do Programa")
#Parte 1 - Gravação do Arquivo
G = "Gravação e Leitura de Arquivo de Texto"
arq = open("Exemplo7_1.txt", "w")
arq.write(G)
arq.close

#Parte 2 - Leitura do arquivo gravado na Parte 1
arq = open("Exemplo7_1.txt", "r")
L = arq.readline()
arq.close()
print("String lido = {}".format(L))
print("Fim do Programa")