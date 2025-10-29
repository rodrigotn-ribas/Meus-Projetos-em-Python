alunos = []  # lista vazia
resultado = " | ".join(alunos)
def escrever():
    for a in alunos:
        # cria uma lista com os valores convertidos em texto
        dados = [a["nome"], str(a["idade"]), a["curso"]]
        linha = ";".join(dados)  # junta tudo com ponto e vírgula
        arquivo.write(linha + "\n")  # grava e pula linha

def ler():
    for linha in arquivo:
        nome, idade, curso = linha.strip().split(";")
        print(f"Nome: {nome} | Idade: {idade} | Curso: {curso}")

    

opcao = input("deseja escrever(w), ler(r), ou adicionar(a): ")
arquivo = open("Roteiro_Estudos/Etapa_4/Arquivos/Dia_1/Lista_alunos.txt", opcao)

while True:
    
    if opcao.lower() == "r":
            ler()
            break
        
    aluno = {}
    aluno["nome"] = input("Nome: ")
    aluno["idade"] = int(input("Idade: "))
    aluno["curso"] = input("Curso: ")
    
    alunos.append(aluno)  # adiciona o dicionário na lista
    
    
    continuar = input("Deseja cadastrar outro aluno? (s/n): ")
    
    if continuar.lower() == "n":
        
        if opcao.lower() == "w" or "a":
            escrever()
            break
    
        arquivo.close()

''' 
    my_list = ["apple", "banana", "cherry"]
    separator = ", "
    joined_string = separator.join(my_list)
    print(joined_string) # Output: apple, banana, cherry
    
    file_name = "output.txt"
    with open(file_name, "w") as file:
        file.write(joined_string)
'''
