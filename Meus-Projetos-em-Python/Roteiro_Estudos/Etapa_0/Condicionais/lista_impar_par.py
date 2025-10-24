'''
Dada uma lista de números, crie duas listas:
Uma com números pares
Outra com números ímpares
'''

num_base = [1,2,3,4,5,6]
par = []
impar = []
for n in num_base:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

print(par)
print(impar)
print(num_base)