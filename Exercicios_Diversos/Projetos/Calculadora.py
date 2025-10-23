
def soma():
    soma = n1 + n2
    print(f"resultado da soma de {n1} + {n2} = {soma}")
    
def subtracao():
    subtracao = n1 - n2
    print(f"resultado da subtracao de {n1} - {n2} = {subtracao}")
    
def multiplicacao():
    multiplicacao = n1 * n2
    print(f"resultado da Multiplicacao de {n1} * {n2} = {multiplicacao}")
    
def divisao():
    divisao = n1 / n2
    print(f"resultado da Divisao de {n1} / {n2} = {divisao}")
    
while True:
    print("Bem vindo a Calculadora")
    print("1 - Soma")
    print("2 - Subtracao")
    print("3 - Multiplicacao")
    print("4 - Divisao")
    print("5 - Sair")
    
    opcao = int(input("Digite uma opcao: "))
    
    if opcao == 5:
        break
    
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