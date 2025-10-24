'''
Use as três funções acima em sequência para montar uma tela simples de apresentação.
'''
def boas_vidas():
    print("Olá, seja bem vindo ao curso de Python")

def mostar_nome_curso(nome, curso):
    print(f"seu nome: {nome}")
    print(f"seu curso: {curso}")

def linha():
    print("-" * 30)

linha()
boas_vidas()
nome = input("digite seu nome: ")
curso = input("digite seu curso: ")
linha()
mostar_nome_curso(nome, curso)
linha()