import pandas as pd
tabela_alunos_df = pd.read_csv('Roteiro_Estudos/Etapa_6/dados_aleatorios_nomes_reais.csv')
tabela_notas_df = pd.read_csv('Roteiro_Estudos/Etapa_6/notas_e_medias.csv')
tabela_final_df = pd.concat([tabela_alunos_df, tabela_notas_df], axis=1)

idade_maior_20 = tabela_final_df.loc[tabela_final_df['idade'] > 20, ["nome", "idade"]]
print(idade_maior_20)


print(tabela_final_df)