import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D


# Heatmap
dados = np.random.rand(10, 10)

plt.imshow(dados, cmap="plasma", interpolation='nearest')
plt.xticks(range(10))
plt.yticks(range(10))
plt.colorbar()
plt.show()

# Grafico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = np.linspace(-5, 5, 30)
Y = np.linspace(-5, 5, 30)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))

ax.plot3D(X, Y, Z, 'blue')
plt.show()

# Temas
plt.style.use('fivethirtyeight')

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.show()

