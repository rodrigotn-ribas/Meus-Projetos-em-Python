'''
Crie uma lista com os números de 1 a 10 e mostre apenas os números pares.
'''
lista = [1,2,3,4,5,6,7,8,9,10]
lista_par = []
for i in lista:
    if i % 2 == 0:
        n = i
        lista_par.append(n)
print(lista_par)