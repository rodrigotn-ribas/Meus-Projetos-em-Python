'''
Crie uma variável global contador = 0.
Depois, crie uma função registrar_chamada() que aumenta esse contador e mostra o número de chamadas.
'''

contador = 0

def registrar_chamada():
    global contador 
    contador += 1
    print(f"quantidades de chamadas {contador}")
    
for i in range(10):
    registrar_chamada()