'''
Crie uma lista com 5 números e:
Mostre o primeiro e o último elemento.
Adicione um novo número no final.
Remova o segundo elemento.
'''

lista = [0,1,2,3,4,5]
print(lista[0])
print(lista[5])
lista.append(6)
print(lista)
lista.insert(7, 7)
print(lista)
lista.pop(1)
print(lista)