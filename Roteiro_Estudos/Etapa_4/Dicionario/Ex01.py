'''
Cadastro simples de alunos
Crie um programa que cadastre nome, idade e curso de vários alunos.
Armazene cada aluno em um dicionário e todos os alunos em uma lista.
Ao final, mostre todos os cadastros no formato:
'''

alunos = {}
for i in range(3):
    nome = input("Digite um nome: ")
    idade = int(input("Digite uma idade: "))
    curso = input("Digite o curso: ")

    aluno = {
        "idade": idade,
        "curso": curso
    }
    alunos[nome] = aluno
    aluno = alunos.get(nome)
    
print(f"Nome: {nome} | Idade: {aluno['idade']} | Curso: {aluno['curso']} |")

