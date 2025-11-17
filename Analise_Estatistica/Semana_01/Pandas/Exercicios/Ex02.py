'''
1) Seleção de dados
Selecione apenas as colunas que você escolher (ex: “age”, “sex”).
Selecione as linhas de índice 10 até 20 usando iloc.
Use loc para pegar as linhas de 0 a 5 e apenas duas colunas.

2) Filtragem simples
Crie filtros como:
Todas as linhas onde Quantidade > 4.
Todas as linhas onde Forma de pagamento = “PIX”.
Todos os registros onde Categoria = “Vestuário” e Preço Unitário > 39.99.
Todos os registros onde uma coluna numérica está entre 10 e 50.

3) DESAFIOS
Filtre todas as linhas onde há mais de 3 colunas nulas.
Filtre usando duas condições compostas com & e |.
'''

import pandas as pd

arquivo = pd.read_csv("Analise_Estatistica/Semana_01/Pandas/tabela_loja.csv")

# ======= Exercicio 1 ======

preco_produto = arquivo[['Produto', 'Preco_Unitario']]
print(preco_produto.loc[10:20])
print(arquivo.loc[0:5, ['Produto', 'Preco_Unitario']])

# ======= Exercicio 2 ======

print(arquivo[arquivo['Quantidade'] > 4])
print(arquivo[arquivo['Forma_Pagamento'] == 'PIX'].head())
print(arquivo[(arquivo['Categoria'] == 'Vestuário') & (arquivo['Preco_Unitario'] > 39.99)])
filtro_intervalo = arquivo[arquivo['Preco_Unitario'].between(10, 50)] # // Mostra os valores da coluna Preco_Unitario estando entre 10 e 50
print(filtro_intervalo)

# ========= Desafio ========
