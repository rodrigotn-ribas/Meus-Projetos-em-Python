'''
Crie um cadastro de alunos onde cada aluno é um dicionário com nome, idade e curso.
Armazene tudo em uma lista.
Mostre cada aluno assim:
Nome: Ana | Idade: 21 | Curso: Computação
'''
alunos = []

while True:
    aluno = {}
    aluno["nome"] = input("Digite o nome: ")
    aluno["idade"] = int(input("Digite a idade: "))
    aluno["curso"] = input("Digite o curso: ")

    alunos.append(aluno)

    continuar = int(input("digite 0 para sair: "))
    if continuar == 0:
        for a in alunos:
            print(f"Nome {a['nome']} | Idade {a['idade']} | Curso {a["curso"]}")
        break

