'''
Crie uma lista chamada numeros com 5 valores inteiros e:
Mostre o primeiro e o último elemento.
Mostre o maior e o menor número.
'''
numeros = [1,2,3,4,5,65,-3]
maior = numeros[0]
menor = numeros[0]

print(numeros[0])
print(numeros[4])

for i in numeros:
    if maior < i:
        maior = i
    if menor > i:
        menor = i
    
print(f"maior numero: {maior}")
print(f"menor numero: {menor}")