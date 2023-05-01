import pandas as pd
import numpy as np

preco = pd.Series([2.1, 7.3, 5.4, 10.9, 6], index= ['Lápis', 'Caneta', 'Borracha', 'Grampeador', 'Apontador'])
print(preco)
preco.index
print(preco['Lápis'])
print(preco.mean())
print(preco.std())
print(preco.describe())

quadrado = preco **2
print(quadrado)

precoLog = np.log(preco)
print('++++++++++++++++++++++++++++++++++++')
print(precoLog)