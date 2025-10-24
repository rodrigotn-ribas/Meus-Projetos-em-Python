'''
Crie uma função que define uma variável local com o mesmo nome de uma variável global e mostre a diferença.
'''
global x
x = 20
def variavel():
    x = 10
    print(x)
print(x) # Recebe o valor da varivale global
variavel() # Recebe o valor da variavel da local