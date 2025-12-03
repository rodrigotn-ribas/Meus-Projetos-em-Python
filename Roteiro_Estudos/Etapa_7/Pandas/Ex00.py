import pandas as pd

# Teste
nome = ['Rodrigo', 'Laura', 'Nicolas', 'Paulo', 'Nicole', 'Sherlock Holmes','Elizabeth Bennet','Jay Gatsby','Hermione Granger','Atticus Finch','Huckleberry Finn','Jane Eyre','Frodo Baggins','Harry Potter','Katniss Everdeen']
idade = [21, 70, 80, 39, 38, 56, 46, 23, 99, 65, 32, 56, 23, 11, 56]
s = pd.Series(nome)
df = pd.DataFrame(idade, nome)
print(df)

# Exericio 1

nome = ['Sherlock Holmes','Elizabeth Bennet','Jay Gatsby','Hermione Granger','Atticus Finch']
idade = [21, 70, 80, 39, 38]
notas = [10, 5.6, 8.9, 10, 3]

df = pd.DataFrame([nome, idade, notas])
print(df.head())
print(df.shape)
print(df,index=nome)
print(df.info())

df = pd.read_csv('Roteiro_Estudos/Etapa_7/Pandas/Tabelas/tabela1.csv')
print(df.head(3))
print(df.shape)
df.set_index('nome', inplace=True)
print(df)
print(df.info())