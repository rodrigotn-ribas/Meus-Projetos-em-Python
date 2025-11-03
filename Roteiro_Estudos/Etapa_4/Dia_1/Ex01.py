'''
Crie um dicionário com informações de uma pessoa (nome, idade, cidade).
Mostre todos os valores formatados.
Adicione uma nova chave profissao.
Exclua a chave idade.
'''
#criando a biblioteca
pessoa = {
    "nome": "Rodrigo",
    "idade": 20,
    "cidade": "Rio de Janeiro" 
}
print(pessoa)

#adicionando profissao
pessoa["profissao"] = "pesquisador"

print(pessoa)

#Excluindo idade
pessoa.pop("idade")

print(pessoa)
