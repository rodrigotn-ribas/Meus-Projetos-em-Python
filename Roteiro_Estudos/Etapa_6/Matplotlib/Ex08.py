import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

df = pd.read_csv("Roteiro_Estudos/Etapa_6/Matplotlib/pokemon.csv")

type_count = df["Type1"].value_counts(ascending=True)

plt.barh(type_count.index, type_count.values, color="#03dffc", edgecolor="black")

plt.title("# of pokemon by Primary Type")
plt.xlabel("Count")
plt.ylabel("Type")
plt.tight_layout()
plt.show()