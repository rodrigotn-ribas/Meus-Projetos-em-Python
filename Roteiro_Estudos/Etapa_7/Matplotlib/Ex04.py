import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Teste
y1 = np.random.rand(50)
x2 = np.random.rand(50)
y2 = np.random.rand(50)
x1 = np.random.rand(50)


plt.plot(x1,y1, color='blue', linestyle='--', marker='o')
plt.scatter(x2, y2, color='red', marker='x' )
plt.show()

# Dados de saude
idade = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
pressao_sanguinea = [120, 122, 125, 130, 135, 140, 145, 150, 155, 160]
colesterol = [180, 185, 190, 195, 200, 205, 210, 215, 220, 225]

plt.plot(idade, pressao_sanguinea, color='blue', linestyle='--', marker='o', label='Pressão Sanguínea')
plt.xlabel('Idade (anos)')
plt.ylabel('Pressão Sanguínea (mmHg)')
plt.show()

# Subplots tetes
fig, ax = plt.subplots(2, 2)   # 1 linha, 2 colunas

x = np.random.rand(50) 
y = np.random.rand(50)
categorias = ["A", "B", "C", "D"]
valores = [10, 20, 15, 30]
dados = np.random.randn(1000)

ax[0,0].plot(x, y)
ax[0,1].scatter(x, y)
ax[1,0].bar(categorias, valores)
ax[1,1].hist(dados)
plt.tight_layout()
plt.show()

# Sublopts

fig, ax = plt.subplots(2,2)

x0 = np.random.rand(50)
y0 = np.random.rand(50)

x1 = [1,2,3,4,5,6,7,8,9,10]
y1 = x1.copy()
for i in range(len(x1)):
    if i % 2 == 0:
        y1[i] = x1[i]+1
    else:
        y1[i] = x1[i]-1

linguagens = ["Python", "C", "C++", "Java"]
valores = [50, 10, 30, 40]

dados = np.random.randn(1000)

ax[0,0].scatter(x0,y0, color = 'red', marker = 's')
ax[0,0].set_title('Scatter')
ax[0,0].set_xlabel('Eixo X')
ax[0,0].set_ylabel('Eixo Y')


ax[0,1].plot(x1,y1, color='green', linestyle='--', marker='o')
ax[0,1].set_title('Linha')
ax[0,1].set_xlabel('Eixo X')
ax[0,1].set_ylabel('Eixo Y')


ax[1,0].bar(linguagens, valores, color=['orange', 'purple', 'blue', 'pink'])
ax[1,0].set_title('barras')
ax[1,0].set_xlabel('Linguagens')
ax[1,0].set_ylabel('Valores')

ax[1,1].hist(dados)
ax[1,1].set_title('histograma')
ax[1,1].set_xlabel('Valores')
ax[1,1].set_ylabel('Frequencia')


plt.tight_layout()
plt.show()

# ==== Exercicio 1 ====
'''
Exercício 1 — Scatter básico
Plote um gráfico de dispersão.
Use cada ponto com cor e tamanho diferentes.
'''
x = np.random.rand(0,100,100)
y = np.random.rand(0,100,100)

plt.scatter(x, y)
# Calcula o ajuste polinomial de grau 1
m, b = np.polyfit(x, y, 1)
# Plota a linha de regressão
plt.plot(x, m*x + b, color='red')
plt.xlabel("Variável X")
plt.ylabel("Variável Y")
plt.title("Gráfico de Dispersão com Linha de Regressão")
plt.show()

# ==== Exercicio 2 ====
'''
Exercício 2 — Scatter + linha
Crie uma tendência com linha (plt.plot)
Coloque os pontos usando plt.scatter
Adicione título e legenda.
'''
x = np.random.randint(0,21,30)
y = np.random.randint(0,21,30)

x1 = [1,2,3,4,5,6,7,8,9,10]
y1 = [1,3,5,7,9,11,13,15,17,19]

plt.plot(x,y)
plt.scatter(x1,y1)
plt.show()

# ==== Exercicio 3 ====
'''
Exercício 3 — Correlação
Crie dados que representem:
correlação positiva
correlação negativa
sem correlação
Plote 3 subplots (1 linha, 3 colunas), um para cada caso.
'''
# correlacao positiva
x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([1,3,5,7,9,11,13,15,17,19])

x1 = x.copy() + 3
y1 = y.copy() + 3

# correlacao negativa
for i in range(len(x)):
    y2 = y.copy() * -1
 
# sem correlacao
x3 = np.array([1,2,3,4,5,6,7,8,9,10])
y3 = np.array([1,1,1,1,1,1,1,1,1,1])

fig, ax = plt.subplots(1,3)

ax[0].plot(x,y, color='red')
ax[0].plot(x,y1, color='blue')
ax[0].set_title('correlacao positiva')


ax[1].plot(x,y, color='red')
ax[1].plot(x,y2, color='blue')
ax[1].set_title('correlacao negativa')


ax[2].plot(x,y, color='red')
ax[2].plot(x3,y3, color='blue')
ax[2].set_title('sem correlacao')


plt.tight_layout()
plt.show()


# ==== Exercicio 4 ====
'''
Exercício 4 — Subplots 2x2
Crie uma figura com 4 gráficos:
linha
dispersão
barra
histograma
Use plt.tight_layout().
'''

x = [1,2,3,4,5,6,7,8,9,10]
y = [1,3,5,7,9,11,13,15,17,19]

x1 = np.random.rand(50)
y1 = np.random.rand(50)

categorias = ["A", "B", "C", "D"]
valores = [10, 20, 15, 30]

dados = np.random.randn(1000)

fig, ax = plt.subplots(2,2)

ax[0,0].plot(x,y, color='red', linestyle='--', marker='o')
ax[0,0].set_title('Linha')

ax[0,1].scatter(x1,y1, color='blue')
ax[0,1].set_title('Scatter')

ax[1,0].bar(categorias,valores, color=['orange', 'purple', 'blue', 'pink'])
ax[1,0].set_title('Barras')

ax[1,1].hist(dados)
ax[1,1].set_title('Histograma')

plt.tight_layout()
# plt.show()


# ==== Exercicio 5 ====
'''
Exercício 5 — Dashboard simples (desafio)
Crie um painel com:
1 scatter (cor variável por valor)
1 barra
1 histograma
todos em um layout 2x2
títulos e labels para tudo
'''
try:
    # Carrega o arquivo de dados dos pinguins
    df_penguins = pd.read_csv('Roteiro_Estudos/Etapa_7/Matplotlib/penguins.csv')

    # Remove linhas onde qualquer uma das colunas usadas nos gráficos seja nula
    df_penguins.dropna(subset=['sex', 'body_mass_g', 'bill_length_mm', 'bill_depth_mm', 'species', 'island'], inplace=True)
    # Filtra os registros para incluir apenas 'MALE' e 'FEMALE', ignorando outros valores.
    df_penguins = df_penguins[df_penguins['sex'].isin(['MALE', 'FEMALE'])]

    # Separa os dados de massa corporal para machos e fêmeas
    massa_machos = df_penguins[df_penguins['sex'] == 'MALE']['body_mass_g']
    massa_femeas = df_penguins[df_penguins['sex'] == 'FEMALE']['body_mass_g']
    # Cria uma tabela de contagem para o gráfico de ilhas vs espécies
    contagem_especies_ilha = pd.crosstab(df_penguins['island'], df_penguins['species'])

    # Cria o gráfico
    fig, ax = plt.subplots(2, 2, figsize=(12, 8))

    # ax[0,0]
    ax[0,0].hist(massa_machos, bins=20, alpha=0.7, label='Machos', color='blue')
    ax[0,0].hist(massa_femeas, bins=20, alpha=0.7, label='Fêmeas', color='red')

    ax[0,0].set_title('Massa corporal dos pinguins', fontsize=16)
    ax[0,0].set_xlabel('Massa Corporal (g)', fontsize=12)
    ax[0,0].set_ylabel('Frequência', fontsize=12)
    ax[0,0].legend()
    ax[0,0].grid(axis='y', linestyle='--', alpha=0.7)

    # ax[0,1]

    largura_bico = df_penguins['bill_length_mm']
    profundidade = df_penguins['bill_depth_mm']
    ax[0,1].scatter(largura_bico, profundidade, c=df_penguins['sex'].map({'MALE': 'blue', 'FEMALE': 'red'}), alpha=0.7)
    ax[0,1].set_title('Profundidade vs Largura do Bico', fontsize=16)
    ax[0,1].set_xlabel('Largura do Bico (mm)', fontsize=12)
    ax[0,1].set_ylabel('Profundidade do Bico (mm)', fontsize=12)
    ax[0,1].grid(axis='both', linestyle='--', alpha=0.7)

    # ax[1,0] - Gráfico de Barras da Distribuição de Espécies
    ax[1,0].bar(df_penguins['species'].unique(), df_penguins['species'].value_counts(), color='green')
    ax[1,0].set_title('Distribuição de Espécies', fontsize=16)
    ax[1,0].set_xlabel('Espécie', fontsize=12)
    ax[1,0].set_ylabel('Frequência', fontsize=12)
    ax[1,0].grid(axis='y', linestyle='--', alpha=0.7)

    # ax[1,1] - NOVO GRÁFICO: Relação Espécies vs Ilhas
    contagem_especies_ilha.plot(kind='bar', ax=ax[1,1], width=0.8)
    ax[1,1].set_title('Distribuição de Espécies por Ilha', fontsize=14)
    ax[1,1].set_xlabel('Ilha', fontsize=12)
    ax[1,1].set_ylabel('Contagem de Pinguins', fontsize=12)
    ax[1,1].tick_params(axis='x', rotation=0) # Deixa o nome das ilhas na horizontal
    ax[1,1].grid(axis='y', linestyle='--', alpha=0.7)


    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print("Arquivo 'penguins.csv' não encontrado. Verifique o caminho do arquivo.")