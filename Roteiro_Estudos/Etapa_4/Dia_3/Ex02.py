'''
Criar um programa que cadastre funcionários e calcule automaticamente
o salário total de cada um (considerando salário base + bônus).
Cada funcionário deve ter:
Nome
Cargo
Salário base
Bônus (%)
Salário total (calculado)
Todos os funcionários são armazenados em uma lista de dicionários.
Ao final, o programa deve:
Mostrar todos os funcionários cadastrados formatados;
Calcular e mostrar a média salarial da empresa.
'''

def display():
    print("\n" + "="*40)
    print("      CADASTRO DE FUNCIONARIO")
    print("="*40)
    print("1. Adicionar novos funcionário")
    print("2. Visualizar todos os funcionários")
    print("3. Calcular média salarial da empresa")
    print("0. Sair")
    print("="*40)

funcionarios = []
salario = 0
while True:
    display()
    opcao = int(input("Digite uma opcao: "))
    funcionario = {}
    
    if opcao == 0:
        break
    
    if opcao == 1:
        funcionario['nome'] = input("Digite seu nome: ")
        funcionario['cargo'] = input("Digite seu cargo: ")
        funcionario['salario base'] = float(input("Digite seu salario base: "))
        funcionario['bonus'] = float(input("Digite seu bonus: "))

        salario = funcionario["salario base"]
        salario += funcionario['salario base']*funcionario['bonus']/100
        funcionario['salario base'] = salario

        funcionarios.append(funcionario)
    
    if opcao == 2:
        for a in funcionarios:
             print(f"Nome: {a['nome']} | Cargo: {a['cargo']} | Salario: {a['salario base']}")
    
    if opcao == 3:
        media = salario/len(funcionario)
        print(f"Media salarial da empresa {salario}")

