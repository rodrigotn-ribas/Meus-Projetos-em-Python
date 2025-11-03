# cria a classe Pizza
class Pedido():
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
            # Usando o método da classe Pizza para exibir os detalhes
            pizza.exibir_pizza()
            total_pedido += pizza.preco

        print(f"\nTOTAL GERAL DO PEDIDO (sem descontos): R$ {total_pedido:.2f}")
    
class Pizza():
    
    def __init__(self, sabor, preco, tamanho):
        self.sabor = sabor
        self.preco = preco
        self.tamanho = tamanho
        
    def exibir_pizza(self):
        print(f"Sabor da pizza: {self.sabor}")
        print(f"Preco sem desconto: {self.preco}")
        print(f"Tamanho da pizza: {self.tamanho}")


        '''
    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError("Nao e permitido uma idade menor que zero")
        self._preco = valor
        '''

    def calcular_preco_com_desconto(self, desconto):
        valor_desconto = self.preco - self.preco * (desconto / 100) 
        print(f"valor com desconto: {valor_desconto}")


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

        
def cadastro():
    sabor = input("digite o sabor da pizza: ")
    preco = float(input("digite o preco da pizza: "))
    tamanho = input("digite o tamanho da pizza: ")  
    novo_pedido = Pizza(sabor, preco, tamanho)
    return novo_pedido
    

# 1. Cadastro da primeira pizza
pizza1 = cadastro() 

# 2. Criação do pedido
pedido1 = Pedido()

# 3. Adiciona a primeira pizza
pedido1.adicionar_pizza(pizza1)

# Exemplo de cálculo de desconto para a pizza1 (opcional)
pizza1.calcular_preco_com_desconto(10) 

# 4. Adiciona uma segunda pizza para testar a lista
pizza2 = Pizza("Calabresa", 45.00, "Grande")
pedido1.adicionar_pizza(pizza2)

pizza3 = PizzaEspecial("Parma", 96, "Gigante", "Rucula")
pedido1.adicionar_pizza(pizza3)

pizza4 = PizzaDoce("Chocolate", 45, "pequena")
pedido1.adicionar_pizza(pizza4)

# 5. Exibe o pedido completo
pedido1.exibir_pedido()