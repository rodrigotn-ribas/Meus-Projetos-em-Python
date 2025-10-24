'''
Dada a lista idades = [12, 18, 25, 30, 15, 22]
Crie uma nova lista apenas com as idades maiores ou iguais a 18.
'''
idades = [12, 18, 25, 30, 15, 22]
idades_maior_idade = []
for i in idades:
    if i >= 18:
        n = i
        idades_maior_idade.append(n)
idades_maior_idade.sort()
print(idades_maior_idade)
