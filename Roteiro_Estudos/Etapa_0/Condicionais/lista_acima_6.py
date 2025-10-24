'''
Faça um programa que receba 10 números e crie uma lista apenas com os que forem maiores que 6.
'''
numeros = []
print("Digite 10 numeros: ")
for i in range(10):
    n = int(input())
    if(n > 6):
        numeros.append(n)

print(numeros)
