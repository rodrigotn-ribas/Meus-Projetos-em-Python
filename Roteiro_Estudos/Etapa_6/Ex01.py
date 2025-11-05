import pandas as pd
tabela_alunos_df = pd.read_csv('Roteiro_Estudos/Etapa_6/dados_aleatorios_nomes_reais.csv')
tabela_notas_df = pd.read_csv('Roteiro_Estudos/Etapa_6/notas_e_medias.csv')
# print(tabela_alunos_df.head()) // mostra as 5 primeiras linhas
# print(tabela_alunos_df.shape) // mostra qnts linhas e colunas
# print(tabela_alunos_df.describe()) // mostra as informacoes mais uteis 
# print(tabela_alunos_df.info()) // mostra colunos, linhas vazias e tipos de objeto

# idade = tabela_alunos_df['idade'] // recebe o valor da coluna idade 

# print(tabela_alunos_df.loc[1:5]) // printa valores de 1 a 5

# idades_maior_20 = (tabela_alunos_df.loc[tabela_alunos_df['idade'] > 20, ["nome", "idade"]] ) // recebe as idades maiores que 20

# tabela_alunos_df['idade + 5'] = tabela_alunos_df['idade'] + 5 // cria uma coluna

# tabela_alunos_df.loc[:, "Media"] = 0 // cria uma coluna com os valores zerados

tabela_final_df = pd.concat([tabela_alunos_df, tabela_notas_df], axis=1)

tabela_final_df = tabela_final_df.drop('media', axis=1)


print(tabela_final_df)
