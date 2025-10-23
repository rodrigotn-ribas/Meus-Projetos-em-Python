'''
Dada a lista numeros = [3, 5, 7, 9, 11]
Multiplique cada elemento por 2 e guarde o resultado em uma nova lista.
'''
lista = [3,5,7,9,11]
lista_mult = []
for n in lista:
    n *= n
    lista_mult.append(n)
print(lista_mult)
