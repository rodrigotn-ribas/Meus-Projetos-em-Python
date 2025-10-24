'''
Crie um programa que leia notas de alunos e as armazene em uma lista de listas, no formato:
alunos = [["Ana", 8.5], ["Bruno", 6.0], ["Clara", 9.0]]
Depois, mostre:
Todos os alunos com nota acima de 7.
A média geral da turma.
'''

alunos = []
alunos_acima_media = []
soma = 0
print("Digite um nome e uma nota: ")
while True:

    nome = input("Nome: ")
    if nome == "sair":
        break

    nota = float(input("Nota: "))

    soma += nota

    alunos.append([nome, nota])

    if nota > 7:
        alunos_acima_media.append([nome, nota])

soma1 = sum(alunos)
media = soma/ len(alunos)
print(alunos)
print(f"Alunos acima da media: {alunos_acima_media}")
print(f"media da turma: {media}")
