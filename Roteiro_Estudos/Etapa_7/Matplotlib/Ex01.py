import matplotlib.pyplot as plt

# ==== Exercicio 1 ====
'''
1) Gráfico simples
Crie um gráfico de linha com:
10 pontos (de 1 a 10 no eixo x)
Valores ao quadrado (x²) no eixo y
Título: “Crescimento Quadrático”
Cor azul
Estilo de linha pontilhado
Grid ativado
'''

x = [1,2,3,4,5,6,7,8,9,10]
y = x.copy()
for i in range(len(x)):
    y[i] = x[i]**2


plt.plot(x,y, color='blue', linestyle='dashed', marker='o')
plt.grid()
plt.title("Crescimento Quadrático")
plt.show()


# ==== Exercicio 2 ====

'''
2) Gráfico estilizado
Crie um gráfico com:
Marcadores circulares
Linha vermelha
Tamanho da figura grande (12 x 6)
Nomes dos eixos personalizados
'''

x = [1,2,3,4,5,6,7,8,9,10]
y = x.copy()
for i in range(len(x)):
    y[i] = x[i]*10

plt.figure(figsize=(12,6))
plt.plot(x,y, color='red', marker='o')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y = x * 10')
plt.show()

plt.savefig('dia1_exercicio3.png')