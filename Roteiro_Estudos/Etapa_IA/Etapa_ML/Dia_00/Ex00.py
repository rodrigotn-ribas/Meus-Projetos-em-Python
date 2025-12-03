import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Criando um dataset simples
x = np.array([1,2,3,4,5,6,7,8,9]).reshape(-1, 1)
y = np.array([2,4,5,4,5,7,8,9,10])

# Divisão dos dados
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Criando o modelo
modelo = LinearRegression()

# Treinando
modelo.fit(x_train, y_train)

# Fazendo previsões
y_pred = modelo.predict(x_test)

# Plotando
plt.scatter(x, y, label="dados reais")
plt.plot(x, modelo.predict(x), label="reta ajustada")
plt.legend()
plt.show()

# Avaliação
print("Coeficiente angular:", modelo.coef_[0])
print("Intercepto:", modelo.intercept_)
print("Score (R²):", modelo.score(x_test, y_test))
