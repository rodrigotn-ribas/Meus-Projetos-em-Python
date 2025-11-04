import funcoes as func

# ===================== CLASSES ===================== #

class Pedido:
    def __init__(self):
        self.itens = []

    def adicionar_pizza(self, pizza):
        self.itens.append(pizza)

    def exibir_pedido(self):
        print("\n=== SEU PEDIDO ===")
        if not self.itens:
            print("O pedido está vazio.")
            return

        total_pedido = 0
        for i, pizza in enumerate(self.itens, 1):
            print(f"\n--- Pizza {i} ---")
            pizza.exibir_pizza()
            total_pedido += pizza.preco

        print(f"\nTOTAL GERAL DO PEDIDO (sem descontos): R$ {total_pedido:.2f}")


class Pizza:
    def __init__(self, sabor, preco, tamanho):
        self.sabor = sabor
        self.preco = preco
        self.tamanho = tamanho

    def exibir_pizza(self):
        print(f"Sabor da pizza: {self.sabor}")
        print(f"Preço sem desconto: R$ {self.preco:.2f}")
        print(f"Tamanho da pizza: {self.tamanho}")

    def calcular_preco_com_desconto(self, desconto):
        valor_desconto = self.preco - self.preco * (desconto / 100)
        print(f"Valor com desconto: R$ {valor_desconto:.2f}")


class PizzaEspecial(Pizza):
    def __init__(self, sabor, preco, tamanho, ingrediente_extra):
        super().__init__(sabor, preco, tamanho)
        self.ingrediente_extra = ingrediente_extra

    def exibir_pizza(self):
        super().exibir_pizza()
        print(f"Ingrediente extra: {self.ingrediente_extra}")


class PizzaDoce(Pizza):
    def __init__(self, sabor, preco, tamanho):
        super().__init__(sabor, preco, tamanho)
        self.preco += 5


# ===================== FUNÇÕES ===================== #

def cardapio_pizza():
    menu_titulo = "Cardápio"
    menu_opcao = [
        "Calabresa - a partir de R$30",
        "Peperoni - a partir de R$40",
        "Mussarela - a partir de R$22",
        "Marguerita - a partir de R$28"
    ]
    cardapio_escolha = func.display_menu(menu_titulo, menu_opcao)

    if cardapio_escolha == 1:
        sabor = "Calabresa"; preco = 30
    elif cardapio_escolha == 2:
        sabor = "Peperoni"; preco = 40
    elif cardapio_escolha == 3:
        sabor = "Mussarela"; preco = 22
    elif cardapio_escolha == 4:
        sabor = "Marguerita"; preco = 28

    print(f"\nAdicionando {sabor}")
    return sabor, preco


def cardapio_tamanho(preco):
    menu_titulo = "Tamanho da Pizza"
    menu_opcao = [
        "Grande - +R$40",
        "Média - +R$30",
        "Pequena - +R$20",
        "Brotinho - sem acréscimo"
    ]
    escolha = func.display_menu(menu_titulo, menu_opcao)

    if escolha == 1:
        tamanho = "Grande"; preco += 40
    elif escolha == 2:
        tamanho = "Média"; preco += 30
    elif escolha == 3:
        tamanho = "Pequena"; preco += 20
    elif escolha == 4:
        tamanho = "Brotinho"

    print(f"\nTamanho selecionado: {tamanho}")
    print(f"Preço total da pizza: R$ {preco:.2f}")
    return tamanho, preco


def cadastro():
    sabor, preco_base = cardapio_pizza()
    tamanho, preco_final = cardapio_tamanho(preco_base)
    nova_pizza = Pizza(sabor, preco_final, tamanho)
    return nova_pizza


# ===================== PONTO DE ENTRADA ===================== #

if __name__ == "__main__":
    func.main()
