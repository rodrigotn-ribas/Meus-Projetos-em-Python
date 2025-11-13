import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Tenta carregar o dataset
try:
    ping = sns.load_dataset("penguins")
except:
    ping = pd.read_csv("penguins.csv")  # se estiver salvo localmente

# Mostra as 5 primeiras linhas
print(ping.head())

# Cria o gráfico de dispersão
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=ping,
    x="bill_length_mm",   # comprimento do bico
    y="body_mass_g",      # massa corporal
    hue="species",        # cores por espécie
    style="sex",          # símbolo diferente para macho/fêmea
    s=100                 # tamanho dos pontos
)

plt.title("Relação entre o tamanho do bico e massa dos pinguins", fontsize=14)
plt.xlabel("Comprimento do bico (mm)")
plt.ylabel("Massa corporal (g)")
plt.legend(title="Espécie")
plt.show()

