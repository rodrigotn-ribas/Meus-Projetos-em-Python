import matplotlib.pyplot as plt
import numpy as np

# Scatter
x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, color='red', s = 50, alpha = 0.5) # s = size
plt.title("Scatter Básico")
plt.show()

# Bar
categorias = ["A", "B", "C", "D"]
valores = [10, 20, 15, 30]

plt.figure(figsize=(8, 6))
plt.bar(categorias, valores, color=['red', 'green', 'blue', 'yellow'], width=0.6)
plt.title("Gráfico de Barras")
plt.show()

# Barh
linguagens = ["Python", "C", "C++", "Java"]
valores = [50, 10, 30, 40]

plt.figure(figsize=(10, 6))
plt.barh(linguagens, valores, color=['orange', 'purple', 'blue', 'pink'])
plt.title("Gráfico de Barras Horizontais")
plt.xlabel("Valores")
plt.ylabel("Linguagens")
plt.show()

# Diferenca entre plot e scatter
x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, color='red', s = 50, marker='o', alpha = 0.5)
plt.title("Scatter Básico")
plt.show()
plt.plot(x,y, color='blue')
plt.show()

# ==== Exercicio 1 ====


'''
1) Scatter com 100 pontos
Crie um scatter com:
100 pontos aleatórios
Cor verde
Marcador '*'
Tamanho variando com um array de 100 valores (ex: s=np.random.randint(20,300,100))
Transparência 0.6
Título: “Distribuição Aleatória”
'''
x = np.random.rand(100)
y = np.random.rand(100)
s=np.random.randint(20,300,100)

plt.scatter(x,y, color='green', marker='*', s=s, alpha=0.6)
plt.title("Distribuição Aleatória")
plt.show()


# ==== Exercicio 2 ====


'''
2) Gráfico de Barras – Vendas Semanais
Categorias: ["Seg", "Ter", "Qua", "Qui", "Sex"]
Valores: [10, 12, 9, 14, 18]
Obrigatório:
Colocar uma cor diferente para cada barra
Exibir o valor acima de cada barra
Nome do gráfico: “Vendas da Semana”
'''
categorias = ["Seg", "Ter", "Qua", "Qui", "Sex"]
valores = [10, 12, 9, 14, 18]

plt.bar(categorias, valores, color=['red', 'green', 'blue', 'yellow', 'orange'], width=0.6, alpha=0.6, edgecolor='black', linewidth=2)
plt.title("Vendas da Semana")

for i, v in enumerate(valores):
    plt.text(i, v, str(v), ha='center', va='bottom')
    # i = posição da barra no eixo X
    # v = altura da barra
    # str(v) = texto que vai aparecer
    # ha = alinhamento horizontal
    # va = alinhamento vertical
plt.show()

# ==== Exercicio 3 ====
'''
3) Barras Horizontais — Ranking
Crie um ranking de 5 personagens, por exemplo:
Personagens: ["Zoggo", "Luna", "Ragnar", "Mira", "Tess"]
Pontuação: [85, 92, 75, 88, 95]
Requisitos:
Gráfico barh
Cores personalizadas
Título “Ranking Final”
'''
personagens = ["Zoggo", "Luna", "Ragnar", "Mira", "Tess"]
pontuacao = [85, 92, 75, 88, 95]

plt.barh(personagens, pontuacao, color = ['red', 'green', 'blue', 'yellow', 'orange'])
plt.title("Ranking Final")
plt.show()

# ==== Exercicio 4 ====
'''
4) Comparação Line x Scatter
Use:
x = range(1, 11)
y = [n * 2 for n in x]
Crie:
um gráfico de linha
um gráfico scatter
coloque ambos como duas figuras separadas
'''

x = range(1, 11)
y = [n * 2 for n in x]

plt.plot(x,y)
plt.title("Grafico de linha")
plt.show()

plt.scatter(x,y)
plt.title("Grafico de Scatter")
plt.show()