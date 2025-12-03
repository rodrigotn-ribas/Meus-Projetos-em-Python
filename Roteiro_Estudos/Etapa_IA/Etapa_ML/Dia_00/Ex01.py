import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# ==== Exercicio 1 ====

# 1. Geração do Conjunto de Dados
# Para garantir que os resultados sejam reproduzíveis, usamos uma semente para o gerador de números aleatórios.
np.random.seed(42)

# Criamos 20 valores para a variável independente (X)
X = np.arange(1, 21).reshape(-1, 1)

# Criamos a variavel valor_aleatorio para gerar os ruidos
valor_aleatorio = np.random.randn(20) * 4

# Criamos a variável dependente (y) com uma relação linear (y = 2*X + 5) e adicionamos um ruído aleatório.
y = 2 * X.flatten() + 5 + valor_aleatorio

# Para facilitar a manipulação, podemos criar um DataFrame do pandas
df = pd.DataFrame({'X': X.flatten(), 'y': y, 'Noise': valor_aleatorio})

print("Conjunto de dados gerado:")
print(df)

# 2. Treinamento do Modelo de Regressão Linear
model = LinearRegression()
model.fit(X, y)

# 3. Visualização dos Dados e da Linha de Regressão
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Dados Originais')
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Linha de Regressão')
plt.title('Regressão Linear Simples')
plt.xlabel('Variável Independente (X)')
plt.ylabel('Variável Dependente (y)')
plt.legend()
plt.grid(True)
plt.show()

# ==== Exercicio 2 ====

np.random.seed(121)

x = np.arange(1, 51).reshape(-1, 1)

valor_aleatorio = np.random.rand(50) * 10

y = 3*x.flatten() + 4 + valor_aleatorio

df = pd.DataFrame({'X' : x.flatten(), 'y' : y, 'Noise' : valor_aleatorio})

print("Conjunto de dados gerado:")
print(df)

model = LinearRegression()
model.fit(x, y)

plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Dados Originais')
plt.plot(x, model.predict(x), color='red', linewidth=2, label='Linha de Regressão')
plt.title('Regressão Linear Simples')
plt.xlabel('Variavel Independente (X)')
plt.ylabel('Variavel Dependente (y)')
plt.legend()
plt.grid(True)
plt.show()

# ==== Exercicio 3 ====
# Gera 
x = np.array([1,2,3,4,5,6,7,8,9]).reshape(-1, 1)
y = np.array([2,4,5,4,5,7,8,9,10])

# Split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Modelo
modelo = LinearRegression()
modelo.fit(x_train, y_train)

# Previsões
y_pred = modelo.predict(x_test)

# Plotando
plt.scatter(x_train, y_train, label="Treino (real)", color="blue")
plt.scatter(x_test, y_test, label="Teste (real)", color="orange")
plt.scatter(x_test, y_pred, label="Previsto", color="red", marker="x", s=100)

# Linha da regressão
plt.plot(x, modelo.predict(x), label="Linha Ajustada", color="green", alpha=0.8)

plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Regressão Linear com Pontos Previstos")
plt.show()

# === Reshape ===
# muda a dimensao da matriz
# Reshaping a 1-D array to a 2-D array
arr_1d = np.array([1, 2, 3, 4, 5, 6])
arr_2d = arr_1d.reshape(2, 3)
arr_teste = arr_1d.reshape(-1,1)
print(f"Original 1D array:\n{arr_1d}")
print(f"Reshaped 2D array:\n{arr_2d}")
print(f"Reshaped 2D array:\n{arr_teste}")

# Reshaping with automatic dimension inference
arr_long = np.array([i for i in range(1, 13)])
arr_inferred_shape = arr_long.reshape(-1, 4)
print(f"Reshaped with inference:\n{arr_inferred_shape}")

# Reshaping to a 3-D array
arr_3d = arr_long.reshape(2, 3, 2)
print(f"Reshaped 3D array:\n{arr_3d}")

# === Flatten ===
# junta todos os valores para uma lista só
nested_list = [[1, 2], [3, 4], [5]]
flattened_list = []
for sublist in nested_list:
    flattened_list.extend(sublist)
print(flattened_list)

X = np.arange(1, 21).reshape(-1, 1)
print(X)
print(X.flatten())

# === Arange ===
# cria uma lista com os valores de 0 a 4
arr = np.arange(5)
print(arr)