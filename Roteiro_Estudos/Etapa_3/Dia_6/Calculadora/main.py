from funcoes import *
while True:
    display()
    opcao = int(input())
    if opcao == 0:
        break
    
    print("Digite dois valores: ")
    a = int(input())
    b = int(input())
    
    if opcao == 1:
        print(f"{a} + {b} =", soma(a,b))
    elif opcao == 2:
        print(f"{a} - {b} =", subtrair(a,b))
    elif opcao == 3:
        print(f"{a} * {b} =", mult(a,b))
    elif opcao == 4:
        print(f"{a} / {b} =", divisao(a,b))
    else:
        print("opcao invalida")