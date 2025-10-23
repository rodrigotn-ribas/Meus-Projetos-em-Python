'''
Crie uma lista com nomes de frutas.
Peça ao usuário uma fruta e diga se ela está na lista ou não.
'''
while True:
    frutas = ["Banana", "Morango", "Uva", "pera", "Abacaxi"]
    Lowercase_frutas = [item.lower() for item in frutas]

    busca = input()

    if busca.lower() in Lowercase_frutas:
        print("correto")
        break
    else:
        print("errado")