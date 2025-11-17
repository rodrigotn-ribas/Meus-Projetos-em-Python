import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


try:
    ping = sns.load_dataset('penguins')
except:
    ping = pd.read_csv("penguins.csv")

# Corrected line: Use histplot for categorical data
plt.figure(figsize=(8, 5)) # Optional: set plot size
sns.histplot(data=ping, x="species", y="sex", col="bill_length_mm", hue="lipper_length_mm")
plt.title('Distribution of Penguin Species')
plt.show() # To display the plot

