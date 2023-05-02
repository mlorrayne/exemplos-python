import pandas as pd

preco = pd.DataFrame({'Produto': ['Lápis', 'Caneta', 'Borracha', 'Grampeador', 'Apontador'], 
                      'Preco': [2.1, 7.3, 5.4, 10.9, 6],
                      'Qtdade': [10, 15, 3, 2, 20],
                      'Custo': [0.5, 1.3, 0.7, 2, 2]})

print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print(preco)

#mostrar nome das colunas
print(preco.columns)

#listar por coluna
print(preco['Produto'])

#ordenação por ordem alfabética
print("Ordem alfabética: ")
print(preco.sort_values(by='Produto'))

#ordenação por ordem crescente de custos
print("Ordem crescente de custos: ")
print(preco.sort_values(by='Custo'))

#ordenação por ordem decrescente de custos
print("Ordem decrescente de custos")
print(preco.sort_values(by='Custo', ascending=False))

#Lógica condicional no DataFrame
print('++++++++++++++++++++++++')
print(preco[preco['Custo']>1.2])

#Usando o & condicional
print(preco[(preco['Custo']>1.2) & (preco['Qtdade']>10)])
