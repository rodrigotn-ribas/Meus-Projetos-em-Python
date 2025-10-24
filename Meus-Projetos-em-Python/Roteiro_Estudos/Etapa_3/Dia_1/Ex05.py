'''
Desafio: crie uma função menu_principal() que mostra um pequeno menu de 3 opções.
'''
def menu_principal():
    print('''--- Bem vindo Professor  ---
--- 1 - Cadastrar Aluno  ---
--- 2 - Verificar lista  ---
--- 3 - Excluir Aluno    ---
--- 4 - Sair do programa ---''')
    
alunos = []

while True:
    menu_principal()
    opcao = int(input())
    if opcao == 1:
        print("Digite o nome do aluno")
        nome = input()
        alunos.append(nome)
    elif opcao == 2:
        for indice, aluno in enumerate(alunos): # valor do indice, para cada aluno dentro da lista alunos
            print(f"{indice+1} {aluno}")
    elif opcao == 3:
        for indice, aluno in enumerate(alunos):
            print(f"{indice+1} {aluno}")
        print("Qual aluno deseja excluir?")
        excluir = int(input("Alunos: "))
        print("Voce esta certo disso?")
        confirmacao = input()
        if confirmacao == "s":
            exclusao = alunos.pop(excluir-1)
    elif opcao == 4:
        break
    else:
        print("digite uma opcao entre as a mostra")
