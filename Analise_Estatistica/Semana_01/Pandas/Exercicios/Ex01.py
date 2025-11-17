'''
1) Trabalhando com DataFrames
1 - Carregue o dataset com read_csv().
2 - Mostre as 5 primeiras linhas.
3 - Mostre as 5 últimas linhas.
4 - Mostre o tipo de cada coluna.
5 - Mostre as dimensões do dataset (linhas x colunas).
6 - Use describe() e interprete 2 valores.
'''

'''
2) Trabalhando com Series
Selecione uma coluna numérica e exiba:
Média
Máximo
Mínimo
Converta essa coluna para uma Series e exiba o tipo.
'''

'''
3) Desafio
Quantas valores únicos existem em alguma coluna categórica?
Liste as 10 primeiras linhas apenas da coluna desejada.
'''

import pandas as pd

arquivo = pd.read_csv("Analise_Estatistica/Semana_01/Pandas/tabela_loja.csv")

# ======= Exercicio 1 ======

print(arquivo.head())
print(arquivo.tail())
print(arquivo.dtypes)
print(arquivo.shape)
print(arquivo.describe())
print(arquivo.info())

# ======= Exercicio 2 ======

print(arquivo['Preco_Unitario'].mean())
print(arquivo['Preco_Unitario'].max())
print(arquivo['Preco_Unitario'].min())
print(arquivo['Preco_Unitario'].dtype)

# ======= Desafio ======

print(arquivo['Categoria'].unique())
print(arquivo['Produto'].head(10))

