import random
lista = []
lista_ordenada = []
for i in range(10):
    n = random.randint(1, 100)
    lista.append(n)

    

print(lista)
lista.sort()
lista_sem_rep = set(lista)
lista_ord_sem_rep = sorted(lista_sem_rep)
print(lista_ord_sem_rep)
print(lista)
print(max(lista))
print(min(lista))
