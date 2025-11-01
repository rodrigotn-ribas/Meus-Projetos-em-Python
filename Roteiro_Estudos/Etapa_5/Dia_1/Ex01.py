# cria a classe Pizza
class Pedido():
    def __init__(self, itens=[]):
        self.itens = itens
        
    def exibir_pedido(self):
        print(f"Seu pedido: {self.itens}")
        
class Pizza():
    
    def __init__(self, sabor, preco, tamanho):
        self.sabor = sabor
        self.preco = preco
        self.tamanho = tamanho
        
    def exibir_pizza(self):
        print(f"Sabor da pizza: {self.sabor}")
        print(f"Preco sem desconto: {self.preco}")
        print(f"Tamanho da pizza: {self.tamanho}")
    
    def calcular_preco_com_desconto(self, desconto):
        valor_desconto = self.preco - self.preco * (desconto / 100) 
        print(f"valor com desconto: {valor_desconto}")
        
def cadastro():
    sabor = input("digite o sabor da pizza: ")
    preco = float(input("digite o preco da pizza: "))
    tamanho = input("digite o tamanho da pizza: ")  
    novo_pedido = Pizza(sabor, preco, tamanho)
    return novo_pedido
    

pizza1 = cadastro()
pedido1 = Pedido(pizza1)
pedido1.exibir_pedido()