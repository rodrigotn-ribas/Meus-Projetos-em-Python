'''
Crie duas listas:
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
Mostre os elementos que estão em ambas as listas.
Mostre os elementos que estão somente em uma delas.
'''
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
lista_ambas = []
lista_somente = []

for i in lista1:
    if i in lista2:
        a = i
        lista_ambas.append(a)
    else:
        s = i
        lista_somente.append(s)

for i in lista2:
    if i in lista2:
        a = i
        lista_ambas.append(a)
    else:
        s = i
        lista_somente.append(s)

lista_ambas1 = set(lista_ambas)
lista_somente1 = set(lista_somente)

print(lista_ambas1)
print(lista_somente1)
    