open("caminho", "r")

# r - leitura
# a - Append / incrementar
# w - Escrita
# x - Criar arquivo
# r+ - Leitura + Escrita

arquivo = open("Roteiro_Estudos/Etapa_4/Arquivos/teste3.txt", "x")

# mostra se pode ser lido
print(arquivo.readable())
# le o arquivo
print(arquivo.read())


lista = arquivo.readlines()

print(lista)
print(lista[3])

arquivo.write("Python\n")
arquivo.close()


import os


if os.path.exists("Roteiro_Estudos/Etapa_4/Arquivos/teste2.txt"):
    os.remove("Roteiro_Estudos/Etapa_4/Arquivos/teste2.txt")
else:
    print("Arquivo n existe")

os.rmdir("Roteiro_Estudos/Etapa_4/Arquivos/nova_pasta")