'''
Faça uma função que modifica uma variável global usando a palavra global.
'''
x = 10
def modifica_variavel():
    global x
    x = 11
    print(x+1)
modifica_variavel() 