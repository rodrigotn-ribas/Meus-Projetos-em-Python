import pandas as pd
import numpy as np

# =============PANDAS=============

# recebe a taleba dos dados na variavel tabela_aluno_df
tabela_aluno_df = pd.read_csv('Roteiro_Estudos/Etapa_6/Exercicios/dados_aleatorios_nomes_reais.csv')

# recebe as idades maiores de 20 anos
alunos_maior_20 = tabela_aluno_df.loc[tabela_aluno_df['idade'] > 20]

# recebe os os valores contados da classe curso. 
relatorio = tabela_aluno_df.groupby('curso')['nome'].count().reset_index()

# cria um arquivo chamado relatorio no formato xlsx
relatorio.to_excel("Roteiro_Estudos/Etapa_6/Exercicios/relatorio_alunos.xlsx", index=False)



# =============NUMPY=============

# cria um array com as idades da tabela
alunos_idade = np.array(tabela_aluno_df['idade'])

# ===========Execucao============

print(f"Media da idade: {alunos_idade.mean()}")
print(f"desvio padrao: {alunos_idade.std()}")
print(f"idade maxima: {alunos_idade.max()}")
print(f"numero de pessoas por cada curso: {relatorio}")

