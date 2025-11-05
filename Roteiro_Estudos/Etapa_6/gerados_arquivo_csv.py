import pandas as pd
import random

# Geração de dados de notas e médias para 100 alunos
notas1 = [round(random.uniform(0, 10), 2) for _ in range(100)]
notas2 = [round(random.uniform(0, 10), 2) for _ in range(100)]
medias = [round((n1 + n2) / 2, 2) for n1, n2 in zip(notas1, notas2)]

# Criando o DataFrame
df_notas = pd.DataFrame({
    "nota1": notas1,
    "nota2": notas2,
    "media": medias
})

# Salvando em CSV
df_notas.to_csv("notas_e_medias.csv", index=False, encoding="utf-8")

print("Arquivo 'notas_e_medias.csv' criado com sucesso!")
