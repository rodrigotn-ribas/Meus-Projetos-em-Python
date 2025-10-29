import os
lista = []
diretorio = 'Roteiro_Estudos/Etapa_4/Arquivos/Dia_1/Mercadinho/'


def escolha_lista():
    for file in os.listdir(diretorio):
        # Verifica se o item é um arquivo e se termina com .txt
        if file.endswith(".txt"):
            new_file = file[:-4]
            print(new_file)
    
def display():
    print("=" * 30)
    print("1 - Cadastrar novo item")
    print("2 - Visualizar Lista")
    print("3 - Criar nova lista")
    print("4 - Excluir lista")
    print("0 - Sair")
    print("=" * 30)

def escreve_item():
    item = input("")
    lista.append(item)
    for items in lista:
        arquivo.write(items + "\n")
    arquivo.close()

while True:
     # escolher como vai ser o formato do arquivo
    display()
    opcao = int(input("digite sua opcao: "))
    
    if opcao == 0:
        break
    
    # Cadastrar Items
    if opcao == 1:
        escolha_lista()
        escolha_arquivo = input() + ".txt"
        formato_arquivo = "a"
        arquivo = open(f"{diretorio}{escolha_arquivo}", formato_arquivo)
        escreve_item()
        
        continuar = input("deseja continuar(s/n): ")
        if continuar.lower() == "n":
           continue
       
    # Visualizar Listas   
    if opcao == 2:
        escolha_lista()
        escolha_arquivo = input() + ".txt"
        if os.path.exists(f"{diretorio}{escolha_arquivo}"):
            formato_arquivo = "r"
            arquivo = open(f"{diretorio}{escolha_arquivo}", formato_arquivo)
            print(arquivo.read())
            arquivo.close()
        else:
            print("nao existe")
            
    # Criar novas Listas
    if opcao == 3:
        formato_arquivo = "w"
        nome_arquivo = input("digite o nome da sua lista: ")
        nome_arquivo += ".txt"
        # Vai criar um novo arquivo com um novo nome
        arquivo = open(f"{diretorio}{nome_arquivo}", formato_arquivo)
        escreve_item()
        
    # Excluir Listas
    if opcao == 4:
        escolha_lista()
        escolha_arquivo = input() + ".txt"
        if os.path.exists(f"{diretorio}{escolha_arquivo}"):
            os.remove(f"{diretorio}{escolha_arquivo}")
        else:
            print("Arquivo n existe") 
        
        