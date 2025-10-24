'''
Escreva um código que receba uma lista de notas (0 a 10) e mostre:
A média das notas
Quantas notas foram acima da média
'''
notas = []
acima_media = []
soma = 0
print("Digite 4 notas")
for i in range(4):
    n = float(input())
    notas.append(n)
    if n > 6:
        acima_media.append(n)
    soma += n
media = soma/4
print(f"suas notas: {notas}")
print(f"Notas acima da media: {acima_media}")
