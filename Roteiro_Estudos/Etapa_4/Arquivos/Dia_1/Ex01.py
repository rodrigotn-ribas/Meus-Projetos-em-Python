alunos = []  # lista vazia

def escrever():
    for item in alunos:
        arquivo.write(f"{item}\n")

def ler():
    print(arquivo.read())

    

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
