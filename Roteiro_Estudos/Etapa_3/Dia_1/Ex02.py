'''
Faça uma função mostrar_nome_curso() que exibe seu nome e o curso que está cursando.
'''

def mostar_nome_curso(nome, curso):
    print(f"seu nome: {nome}")
    print(f"seu curso: {curso}")

nome = input("digite seu nome: ")
curso = input("digite seu curso: ")

mostar_nome_curso(nome, curso)