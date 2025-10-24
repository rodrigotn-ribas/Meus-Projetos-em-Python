'''
Desafio: crie uma função par_ou_impar(n) que retorna "par" ou "ímpar" e use dentro de um programa principal.
'''
def par_ou_impar(n):
    if n % 2 == 0:
        par = "par"
        return par
    else:
        impar = "impar"
        return impar

resultado = par_ou_impar(5)
print(resultado)