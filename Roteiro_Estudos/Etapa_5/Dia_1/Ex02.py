class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def exibir_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Páginas: {self.paginas}")

def criar_livro_com_input():
    """
    Função que solicita dados ao usuário via input()
    e cria um objeto Livro.
    """
    print("--- Cadastro de Novo Livro ---")
    # Captura a entrada como string
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    
    # Captura a entrada e converte para inteiro (int)
    paginas = int(input("Digite o número de páginas: ")) #
    
    # Cria o objeto usando os valores do input
    novo_livro = Livro(titulo, autor, paginas)
    
    # Retorna o objeto criado
    return novo_livro

# Uso:
# Chama a função para criar o objeto
livro_usuario = criar_livro_com_input()

# Acessa o objeto retornado e chama um método
print("\n--- Informações do Livro Cadastrado ---")
livro_usuario.exibir_info()
