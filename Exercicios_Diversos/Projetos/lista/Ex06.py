'''
Peça nomes ao usuário até que ele digite "sair".
No final, exiba todos os nomes digitados em ordem alfabética.
'''
nomes = []
opcao = ""
print("Digite Nomes(digite sair para sair):")
while True:
    opcao = input("Digite um nome: ")
    if opcao == "sair":
        break
    nomes.append(opcao)
nomes.sort()
print(nomes)