import matplotlib.pyplot as plt
import numpy as np

# Plot
x1 = [1,2,3,4,5,6,7,8,9,10]
y1 = x1.copy()
for i in range(len(x1)):
    if i % 2 == 0:
        y1[i] = x1[i]+1
    else:
        y1[i] = x1[i]-1

x2 = [1,2,3,4,5,6,7,8,9,10]
y2 = x2.copy()
for i in range(len(x2)):
    if i % 2 == 1:
        y2[i] = x2[i]+1
    else:
        y2[i] = x2[i]-1

x3 = [1,2,3,4,5,6,7,8,9,10]
y3 = x3.copy()
for i in range(len(x2)):
    if i % 2 == 1:
        y3[i] = x3[i]+2
    else:
        y3[i] = x3[i]-2

plt.figure(figsize=(10,6))
plt.plot(x1, y1,label='par', color='#a80826',marker='^', alpha=1, linestyle='-')
plt.plot(x2, y2,label='impar', color="#400fe0",marker='s', alpha=1, linestyle=':')
plt.plot(x3, y3,label='gold', color="#e0d20f",marker='o', alpha=1, linestyle='-.')
plt.title("plot teste")
plt.legend()
plt.show()


# Bar
categorias = ["A", "B", "C", "D"]
valores = [10, 20, 15, 30]

plt.figure(figsize=(8, 6))
plt.bar(categorias, valores, color=['#FFD700', '#8A2BE2', (0.2, 0.5, 0.9), '#FA8072'], width=0.6, edgecolor = 'black', linewidth=2)
plt.title("Gráfico de Barras")
plt.show()

# ==== Exercicio 1 ====
'''
Exercício 1 — Personalização básica
Crie um gráfico de linha com:
linha tracejada
cor roxa
espessura de 3
marcadores circulares
Use qualquer lista de valores.
'''
x = [1,2,3,4,5,6,7,8,9,10]
y = [1,3,5,7,9,11,13,15,17,19]
plt.plot(x,y, color='purple', linewidth = 3, marker ='o', linestyle = '--')
plt.show()
# ==== Exercicio 2 ====
'''
Exercício 2 — Duas linhas
Plote duas listas diferentes no mesmo gráfico:
uma azul sólida
outra vermelha pontilhada
adicione legenda
'''
x = [1,2,3,4,5,6,7,8,9,10]
y = [1,3,5,7,9,11,13,15,17,19]
y2 = [2,4,6,8,10,12,14,16,18,20]
plt.plot(x,y, color='blue', label='azul')
plt.plot(x,y2, color='red', linestyle=':', label='vermelha')
plt.legend()
plt.show()
# ==== Exercicio 3 ====
'''
Exercício 3 — Gráfico completo
Crie um gráfico com:
título
rótulos dos eixos
duas linhas com estilos diferentes
limites personalizados
marcadores
legenda
grade (plt.grid())
'''
x = [1,2,3,4,5,6,7,8,9,10]
y = [1,3,5,7,9,11,13,15,17,19]
y2 = [2,4,6,8,10,12,14,16,18,20]
plt.plot(x,y, linestyle='-.', marker='s', color='red', label ='vermelho')
plt.plot(x,y2, linestyle='--', marker='o', color='blue', label='blue')
plt.title('Titulo')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.grid()
plt.legend()
plt.show()
# ==== Exercicio 4 ====
'''
Exercício 4 — Três linhas com estilos variados
Crie um gráfico com 3 séries, cada uma usando:
estilo de linha diferente
cor diferente
marcador diferente
'''
x = [1,2,3,4,5,6,7,8,9,10]
y = [1,3,5,7,9,11,13,15,17,19]
y2 = [2,4,6,8,10,12,14,16,18,20]
y3 = [3,5,7,9,11,13,15,17,19,21]
plt.plot(x,y, linestyle='-.', marker='s', color='red', label ='vermelho')
plt.plot(x,y2, linestyle='--', marker='o', color='blue', label='blue')
plt.plot(x,y3, linestyle=':', marker='^', color='green', label='verde')
plt.title('Titulo')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.grid()
plt.legend()
plt.show()

# ==== Exercicio 5 ====
'''
Exercício 5 — Criatividade
Invente qualquer série numérica e faça um gráfico altamente personalizado, usando:
cor personalizada (hex)
marcador e linha
título estilizado
limites de eixos
grade
legenda
'''

x = [1,2,3,4,5,6,7,8,9,10]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
y3 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
plt.plot(x,y, linestyle='-.', marker='s', color='red', label ='vermelho')
plt.plot(x,y2, linestyle='--', marker='o', color='blue', label='blue')
plt.plot(x,y3, linestyle=':', marker='^', color='green', label='verde')
plt.title('Titulo')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.grid()
plt.legend()
plt.show()
