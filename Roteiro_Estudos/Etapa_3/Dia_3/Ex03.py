'''
Escreva uma função maior(a, b) que retorna o maior valor entre dois números.
'''
def maior(a,b):
    if a > b:
        maior = a
    else:
        maior = b
    return maior

resultado = maior(2,3)
print(resultado)