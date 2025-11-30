import numpy as np
import matplotlib.pyplot as plt

# Teste
# y1 = np.random.rand(50)
# x2 = np.random.rand(50)
# y2 = np.random.rand(50)
# x1 = np.random.rand(50)


# plt.plot(x1,y1, color='blue', linestyle='--', marker='o')
# plt.scatter(x2, y2, color='red', marker='x' )
# plt.show()

# Dados de saude
idade = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
pressao_sanguinea = [120, 122, 125, 130, 135, 140, 145, 150, 155, 160]
colesterol = [180, 185, 190, 195, 200, 205, 210, 215, 220, 225]

plt.plot(idade, pressao_sanguinea, color='blue', linestyle='--', marker='o', label='Pressão Sanguínea')
plt.xlabel('Idade (anos)')
plt.ylabel('Pressão Sanguínea (mmHg)')
plt.show()