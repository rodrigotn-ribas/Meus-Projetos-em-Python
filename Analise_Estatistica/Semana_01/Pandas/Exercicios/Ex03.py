'''
1) Valores nulos
Descubra quantos valores nulos existem em cada coluna.
Liste apenas as colunas que têm nulos.
Remova todas as linhas com nulos (teste e veja o resultado).
Preencha valores nulos de uma coluna numérica com a média.
Preencha valores nulos de uma coluna categórica com o valor “Desconhecido”.

2) Ajuste e padronização
Renomeie 3 colunas (ex.: “Age” → “idade”).
Remova colunas que não vai usar.
Converta uma coluna para int ou float com astype.
Converta uma coluna categórica para category.

3) DESAFIOS
Remova linhas duplicadas.
Crie uma nova coluna com base em outra (ex: idade > 18 → “adulto/menor”).
'''

import pandas as pd

arquivo = pd.read_csv('Analise_Estatistica/Semana_01/Pandas/tabela_loja.csv')

# ======= Exercicio 01 =======

print(arquivo.isnull().sum())

# colunas_nulas = arquivo.columns[arquivo.isnull().any()]
# print(colunas_nulas)

# arquivo.dropna(inplace=True)
# print(arquivo)

# arquivo["Preco_Unitario"] = arquivo["Preco_Unitario"].fillna(arquivo["Preco_Unitario"].mean())
# print(arquivo)

# arquivo["Categoria"] = arquivo["Categoria"].fillna('Desconhecido')
# print(arquivo)

# ======= Exercicio 02 =======

