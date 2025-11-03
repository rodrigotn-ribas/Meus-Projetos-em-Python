'''
Crie um programa de cadastro de produtos:
Campos: nome, preço e quantidade.
Permita adicionar novos produtos.
Mostre todos os produtos.
Calcule o valor total do estoque.
Exemplo de saída:
Produto: Pizza Calabresa | Preço: 45 | Quantidade: 3
Valor total em estoque: R$135
'''
def display():
    print("\n" + "="*40)
    print("      CADASTRO DE PRODUTOS")
    print("="*40)
    print("1. Adicionar novos produtos")
    print("2. Visualizar todos os produtos")
    print("3. Calcular valor de estoque")
    print("0. Sair")
    print("="*40)

produtos = []
valor_estoque = 0
while True:

    display()

    opcao = int(input())

    if opcao == 0:
        break

    if opcao == 1:

        produto = {}

        produto['nome'] = input("Digite o nome: ")
        produto['preco'] = float(input("Digite o preco: "))
        produto['quantidade'] = int(input("Digite a quantidade: "))
        valor_estoque += produto['preco']

        produtos.append(produto)
    
    if opcao == 2:
        for a in produtos:
            print(f"Nome: {a['nome']} | Preco: R${a['preco']} | Quantidade: {a["quantidade"]}")
        
    if opcao == 3:
        print(f"valor total do estoque R${valor_estoque}")
