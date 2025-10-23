'''
Peça ao usuário números até ele digitar 0.
Guarde todos os números em uma lista e, no final, mostre:
Quantos números foram digitados
A soma deles
A média
'''
numeros = []
num_digitado = []
soma = 0
while True:
    print("digite valores, menos 0")
    n = int(input())
    soma += n
    if(n == 0):
        media = soma/len(numeros)
        print(numeros)
        print(len(numeros))
        print(soma)
        print(media)
        break
    numeros.append(n)

