'''
Peça 5 números ao usuário e guarde em uma lista.
Depois, exiba a soma e a média dos números.
'''
lista = []
soma = 0
for i in range(5):
    n = int(input(f"Digite 0{i+1} valores: "))
    lista.append(n)
    soma += n

media = soma/5 
soma1 = sum(lista) #método sum faz a soma de uma lista
print(soma1)
print(soma)
print(media)