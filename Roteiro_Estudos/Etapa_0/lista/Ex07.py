'''
Crie uma lista com 10 números aleatórios entre 1 e 50 (use random.randint).
Mostre:
O maior e o menor número.
A lista ordenada de forma crescente.
'''
import random

lista = []

for i in range(10):  
    n = random.randint(1,50)
    lista.append(n)
print(max(lista))
print(min(lista))
lista.sort()
print(lista)