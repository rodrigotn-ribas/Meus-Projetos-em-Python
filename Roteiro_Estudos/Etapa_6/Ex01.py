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

tabela_final_df = pd.concat([tabela_alunos_df, tabela_notas_df], axis=1) # axis = 1 : coluna; axis = 0 : linha;

# tabela_final_df = tabela_final_df.drop('media', axis=1) // retira a coluna media

# tabela_final_df = tabela_final_df.dropna(how='all', axis=1) // exclui uma coluna ou uma linha

# tabela_final_df = tabela_final_df.dropna(how='all', axis=1) // exclui linhas com ao menos um valor vazio 

# tabela_final_df['media'] = tabela_final_df['media'].fillna(tabela_alunos_df['media'].mean) // preenche os valores vazios com a media das medias

# tabela_final_df = tabela_alunos_df.ffill // preenche os valores NAN com o primeiro valor de cima

# cursos = tabela_final_df['curso'].value_counts() // mostra valor por cada curso

# media_curso = tabela_final_df[['curso', 'media']].groupby('curso').mean() // mostra a media de cada curso

nota_max = tabela_final_df.max()

print(nota_max)
