'''
Lista de Compras
Regras:
O usuário digita itens até escrever “sair”.
Os itens são guardados em uma lista.
No final, o programa mostra todos os itens adicionados e quantos são.
Desafio extra:
Faça uma versão que não permita adicionar o mesmo item duas vezes.
'''

lista = []
item = ""
print("Digite seus itens")
while True:
    item = input() # recebe o valor do item
    if item == "sair": # se intem igual a sair, termina o programa
        break
    if item in lista:
        print("--- nao e possivel adicionar o mesmo item na lista ---")
    else:
        lista.append(item) # adiciona os itens da lista
print(lista) # imprime a lista
print(f"tamanho da lista: {len(lista)}") # imprime o tamanho da lista
