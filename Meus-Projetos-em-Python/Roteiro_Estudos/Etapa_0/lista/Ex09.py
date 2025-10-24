'''
Dada a lista palavras = ["casa", "carro", "avião", "bicicleta", "barco"]
Crie uma nova lista contendo apenas as palavras com mais de 4 letras.
'''
lista = ["casa", "carro", "avião", "bicicleta", "barco"]
lista_4_mais = []
for s in lista:
    if len(s) > 4:
        lista_4_mais.append(s)
print(lista_4_mais)