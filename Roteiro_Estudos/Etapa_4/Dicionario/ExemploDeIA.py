# Sistema de Cadastro de Alunos

# Dicionário principal para armazenar os alunos
# A chave será a matrícula e o valor será outro dicionário com os dados do aluno
alunos = {}

def menu():
    """Exibe o menu principal"""
    print("\n" + "="*40)
    print("      SISTEMA DE CADASTRO DE ALUNOS")
    print("="*40)
    print("1. Cadastrar novo aluno")
    print("2. Buscar aluno por matrícula")
    print("3. Listar todos os alunos")
    print("4. Atualizar dados do aluno")
    print("5. Remover aluno")
    print("6. Estatísticas")
    print("0. Sair")
    print("="*40)

def cadastrar_aluno():
    """Cadastra um novo aluno no sistema"""
    print("\n--- CADASTRAR NOVO ALUNO ---")
    
    try:
        matricula = input("Digite a matrícula do aluno: ").strip()
        
        # Verifica se a matrícula já existe
        if matricula in alunos:
            print("❌ Erro: Matrícula já cadastrada!")
            return
        
        nome = input("Digite o nome do aluno: ").strip()
        idade = int(input("Digite a idade do aluno: "))
        curso = input("Digite o curso do aluno: ").strip()
        nota = float(input("Digite a nota do aluno (0-10): "))
        
        # Validação da nota
        if nota < 0 or nota > 10:
            print("❌ Erro: Nota deve estar entre 0 e 10!")
            return
        
        # Criando o dicionário do aluno
        aluno = {
            "nome": nome,
            "idade": idade,
            "curso": curso,
            "nota": nota
        }
        
        # Adicionando ao dicionário principal
        alunos[matricula] = aluno
        print(f"✅ Aluno {nome} cadastrado com sucesso!")
        
    except ValueError:
        print("❌ Erro: Idade deve ser um número inteiro e nota um número decimal!")

def buscar_aluno():
    """Busca um aluno pela matrícula"""
    print("\n--- BUSCAR ALUNO ---")
    
    matricula = input("Digite a matrícula do aluno: ").strip()
    
    # Usando get() para buscar o aluno
    aluno = alunos.get(matricula)
    
    if aluno:
        print(f"\n📋 Dados do aluno:")
        print(f"Matrícula: {matricula}")
        print(f"Nome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']} anos")
        print(f"Curso: {aluno['curso']}")
        print(f"Nota: {aluno['nota']:.1f}")
    else:
        print("❌ Aluno não encontrado!")

def listar_alunos():
    """Lista todos os alunos cadastrados"""
    print("\n--- LISTA DE ALUNOS ---")
    
    if not alunos:
        print("Nenhum aluno cadastrado no sistema.")
        return
    
    for matricula, aluno in alunos.items():
        print(f"\nMatrícula: {matricula}")
        print(f"Nome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']} anos")
        print(f"Curso: {aluno['curso']}")
        print(f"Nota: {aluno['nota']:.1f}")
        print("-" * 20)

def atualizar_aluno():
    """Atualiza os dados de um aluno existente"""
    print("\n--- ATUALIZAR DADOS DO ALUNO ---")
    
    matricula = input("Digite a matrícula do aluno: ").strip()
    
    if matricula not in alunos:
        print("❌ Aluno não encontrado!")
        return
    
    aluno = alunos[matricula]
    print(f"\nAluno encontrado: {aluno['nome']}")
    
    print("\nO que deseja atualizar?")
    print("1. Nome")
    print("2. Idade")
    print("3. Curso")
    print("4. Nota")
    print("5. Todos os dados")
    
    try:
        opcao = input("Escolha uma opção (1-5): ").strip()
        
        if opcao == "1":
            novo_nome = input("Novo nome: ").strip()
            aluno["nome"] = novo_nome
            print("✅ Nome atualizado!")
            
        elif opcao == "2":
            nova_idade = int(input("Nova idade: "))
            aluno["idade"] = nova_idade
            print("✅ Idade atualizada!")
            
        elif opcao == "3":
            novo_curso = input("Novo curso: ").strip()
            aluno["curso"] = novo_curso
            print("✅ Curso atualizado!")
            
        elif opcao == "4":
            nova_nota = float(input("Nova nota (0-10): "))
            if 0 <= nova_nota <= 10:
                aluno["nota"] = nova_nota
                print("✅ Nota atualizada!")
            else:
                print("❌ Nota deve estar entre 0 e 10!")
                
        elif opcao == "5":
            aluno["nome"] = input("Novo nome: ").strip()
            aluno["idade"] = int(input("Nova idade: "))
            aluno["curso"] = input("Novo curso: ").strip()
            nova_nota = float(input("Nova nota (0-10): "))
            if 0 <= nova_nota <= 10:
                aluno["nota"] = nova_nota
                print("✅ Todos os dados atualizados!")
            else:
                print("❌ Nota deve estar entre 0 e 10!")
        else:
            print("❌ Opção inválida!")
            
    except ValueError:
        print("❌ Erro: Digite valores numéricos válidos!")

def remover_aluno():
    """Remove um aluno do sistema"""
    print("\n--- REMOVER ALUNO ---")
    
    matricula = input("Digite a matrícula do aluno: ").strip()
    
    if matricula in alunos:
        aluno = alunos[matricula]
        confirmacao = input(f"Tem certeza que deseja remover {aluno['nome']}? (s/n): ").strip().lower()
        
        if confirmacao == 's':
            del alunos[matricula]
            print("✅ Aluno removido com sucesso!")
        else:
            print("Operação cancelada.")
    else:
        print("❌ Aluno não encontrado!")

def estatisticas():
    """Exibe estatísticas do sistema"""
    print("\n--- ESTATÍSTICAS ---")
    
    total_alunos = len(alunos)
    print(f"Total de alunos cadastrados: {total_alunos}")
    
    if total_alunos > 0:
        # Calcula a média das notas
        notas = [aluno["nota"] for aluno in alunos.values()]
        media_notas = sum(notas) / total_alunos
        
        # Encontra a maior e menor nota
        maior_nota = max(notas)
        menor_nota = min(notas)
        
        # Conta alunos por curso
        cursos = {}
        for aluno in alunos.values():
            curso = aluno["curso"]
            cursos[curso] = cursos.get(curso, 0) + 1
        
        print(f"Média das notas: {media_notas:.2f}")
        print(f"Maior nota: {maior_nota:.1f}")
        print(f"Menor nota: {menor_nota:.1f}")
        
        print("\nAlunos por curso:")
        for curso, quantidade in cursos.items():
            print(f"  {curso}: {quantidade} aluno(s)")

# Programa principal
def main():
    """Função principal do sistema"""
    print("Bem-vindo ao Sistema de Cadastro de Alunos!")
    
    while True:
        menu()
        
        opcao = input("\nDigite sua opção: ").strip()
        
        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            buscar_aluno()
        elif opcao == "3":
            listar_alunos()
        elif opcao == "4":
            atualizar_aluno()
        elif opcao == "5":
            remover_aluno()
        elif opcao == "6":
            estatisticas()
        elif opcao == "0":
            print("\nObrigado por usar o sistema! Até logo! 👋")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")
        
        input("\nPressione Enter para continuar...")

# Executa o programa
if __name__ == "__main__":
    main()