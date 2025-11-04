def display_menu(titulo, opcao):
    print("\n" + "=" * 40)
    print(f"{titulo.center(40)}")
    print("=" * 40)

    for i, item in enumerate(opcao, 1):
        print(f"{i}. {item}")

    print("=" * 40)

    while True:
        try:
            escolha = int(input("Digite sua escolha: "))
            if 1 <= escolha <= len(opcao):
                return escolha
            else:
                print("Escolha inválida. Digite um número dentro do intervalo.")
        except ValueError:
            print("Entrada inválida. Digite um número.")


def main():
    import Projeto_Pizza as pp  # import dentro da função evita import circular

    pedido = pp.Pedido()  # mantém o mesmo pedido durante a execução
    menu_titulo = "Bem-vindo à Pizzaria PY"
    menu_opcao = ["Cardápio", "Carrinho", "Sair"]

    while True:
        usuario_escolha = display_menu(menu_titulo, menu_opcao)

        if usuario_escolha == 1:
            while True:
                pizza = pp.cadastro()
                pedido.adicionar_pizza(pizza)
                print(f"\nPizza de {pizza.sabor} adicionada ao seu pedido!")

                continuar = input("Deseja adicionar outra pizza? (s/n): ")
                if continuar.lower().strip() != 's':
                    break

        elif usuario_escolha == 2:
            pedido.exibir_pedido()

        elif usuario_escolha == 3:
            print("\nSaindo do sistema... Até logo!")
            break
