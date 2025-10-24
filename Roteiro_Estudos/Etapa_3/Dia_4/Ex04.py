'''
Desafio: crie um contador global de quantas vezes o usuário executa diferentes funções do programa.
'''
contador = 0

def soma():
    global contador
    contador += 1
    soma = n1 + n2
    print(f"resultado da soma de {n1} + {n2} = {soma}")
    
def subtracao():
    global contador
    contador += 1
    subtracao = n1 - n2
    print(f"resultado da subtracao de {n1} - {n2} = {subtracao}")
    
def multiplicacao():
    global contador
    contador += 1
    multiplicacao = n1 * n2
    print(f"resultado da Multiplicacao de {n1} * {n2} = {multiplicacao}")
    
def divisao():
    global contador
    contador += 1
    divisao = n1 / n2
    print(f"resultado da Divisao de {n1} / {n2} = {divisao}")
    
while True:
    print("-" * 20)
    print("Bem vindo a Calculadora")
    print("1 - Soma")
    print("2 - Subtracao")
    print("3 - Multiplicacao")
    print("4 - Divisao") 
    print("5 - Mostrar contador")
    print("6 - Sair")
    print("-" * 20)
    
    opcao = int(input("Digite uma opcao: "))
    
    if opcao == 6:
        break
    
    elif opcao == 5:
        print(contador)
    
    print("Digite dois valores: ")
    n1 = float(input())
    n2 = float(input())
    
    if opcao == 1:
        soma()
         
    elif opcao == 2:
        subtracao()
         
    elif opcao == 3:
        multiplicacao()
         
    elif opcao == 4:
        divisao()
    
    
    else:
        print("opaco invalida")