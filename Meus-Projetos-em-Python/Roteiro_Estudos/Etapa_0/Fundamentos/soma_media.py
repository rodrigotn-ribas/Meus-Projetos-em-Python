"""
Peça 5 números ao usuário e salve em uma lista.
Depois, mostre a soma e a média deles.

"""
'''
lista_de_numeros = [1, 2, 3, 4, 5]
total = sum(lista_de_numeros)
print(total) # Saída: 15
'''
print("Digite 5 valores para uma lista")
soma=0
numeros = []
for i in range(5):
    valor = int(input())
    numeros.append(valor)
    soma += valor

media = soma/5

print(f"Soma = {soma}")
print(f"Media = {media}")

