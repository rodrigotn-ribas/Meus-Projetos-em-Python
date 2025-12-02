import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# histograma
# dados1 = np.random.randn(1000)
# dados2 = np.random.randn(1000)

# plt.hist(dados1, bins=20, color='skyblue', edgecolor='black', alpha=0.4)
# plt.hist(dados2, bins=20, color='red', edgecolor='black', alpha=0.4)

# arquivo = pd.read_csv('Roteiro_Estudos/Etapa_7/Matplotlib/covid19.csv')
# print(arquivo.shape)

# date = arquivo['Date']
# death_usa = arquivo['US']

# plt.plot(date, death_usa, color='red', linestyle='--',)
# plt.show()

# Boxplot
# x = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100]
# y = [-10,-20,-30,-40,-50,-60,-70,-80,-90,-100,1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100]

# plt.boxplot([x,y], patch_artist=True, boxprops=dict(facecolor='lightgreen'))
# plt.show()

# Violin plot

# plt.violinplot([x,y])
# plt.show()

# Sub-plot

# fig, ax = plt.subplots(1,3, figsize=(12,6))

# dados1 = np.random.randn(1000)
# dados2 = np.random.randn(1000)

# ax[0].hist(dados1, bins=20, color='skyblue', edgecolor='black', alpha=0.4)
# ax[0].hist(dados2, bins=20, color='red', edgecolor='black', alpha=0.4)

# ax[1].boxplot([x,y], patch_artist=True, boxprops=dict(facecolor='blue'))

# ax[2].violinplot([x,y])

# plt.tight_layout()
# plt.show()

# ==== Exercicio 1 ====
'''
Exercício 1 – Histograma simples
Crie um histograma com:
20 bins
cor personalizada
borda preta
título e labels
'''
# dados = np.random.randn(1000)
# plt.hist(dados, bins=20, color='orange', edgecolor='black', label = 'dados')
# plt.legend()
# plt.title('Histograma')
# plt.show()
# ==== Exercicio 2 ====
'''
Exercício 2 – Comparação de dois conjuntos
Gere dois conjuntos de dados (normal e uniforme) e compare usando:
um histograma sobreposto
e um subplot 1x2 com dois boxplots
'''
# dados_normal = np.random.randn(1000)
# dados_uniforme = np.random.rand(1000)

# fig, ax = plt.subplots(1,2, figsize=(12,6))

# ax[0].hist(dados_normal, bins=20, color='skyblue', edgecolor='black', alpha=0.4, label='normal')
# ax[1].hist(dados_uniforme, bins=20, color='red', edgecolor='black', alpha=0.4, label='uniforme')

# ax[0].legend()
# ax[1].legend()

# plt.tight_layout()
# plt.show()
# ==== Exercicio 3 ====
'''
Exercício 3 – Boxplot completo
Crie um boxplot mostrando 3 séries de dados diferentes, cada uma com:
cor diferente
título
rótulo no eixo X
'''
# x = [1,2,3,4,5,6,7,8,9,10]
# y = [1,3,5,7,9,11,13,15,17,19]
# z = [2,4,6,8,10,12,14,16,18,20]

# plt.boxplot([x,y,z], patch_artist=True, boxprops=dict(facecolor='blue'))
# plt.show()
# ==== Exercicio 4 ====
'''
Exercício 4 – Violin vs Boxplot
Faça um subplot 1x2:
violin plot
boxplot
Usando o mesmo conjunto de dados.
Compare visualmente.
'''
# x = np.random.rand(1000)

# fig, ax = plt.subplots(1,2, figsize=(12,6))

# ax[0].violinplot(x)
# ax[1].boxplot(x)

# plt.tight_layout()
# plt.show()

# ==== Exercicio 5 ====
'''
Exercício 5 – Dashboard de Distribuições (desafio)
Crie um dashboard 2x2 contendo:
histograma
boxplot
violin plot
scatter plot entre dois conjuntos
Todos com título e labels.
'''
# dados = np.random.randn(1000)
# x = [1,2,3,4,5,6,7,8,9,10]
