 # Criando Dicionario
pessoa = {'nome': 'Matheus','idade': 34}

# Ou - pessoa = dict(nome='Matheus', idade=34)
#--------------------------------------------------------
# Adicionando nova chave
pessoa['telefone'] = '3333-4444'

print(pessoa)
print()
#--------------------------------------------------------
# Acesso aos dados
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['telefone'])
print()
#--------------------------------------------------------
# Sobre escrecendo os dados
(pessoa['nome']) = 'Maria'
(pessoa['idade']) = 18
(pessoa['telefone']) = '1111-2222'
print(pessoa)
print()
#--------------------------------------------------------
# Dicionários Aninhados
contatos = {
    '001': {'nome':'Matheus', 'telefone':'1111-2222'},
    '002': {'nome':'Ana', 'telefone':'1111-2221'},
    '003': {'nome':'Maria', 'telefone':'1111-2223'},
    '004': {'nome':'João', 'telefone':'1111-2224','004-1':{'a':1}}
}

print(contatos['001']['nome'])
print(contatos['002'])
print(contatos['004']['004-1']['a']) #Dicionario dentro de outro
print()
#--------------------------------------------------------
# Iterar Dicionários
for chave in contatos:
    print(chave, contatos[chave])

# for chave, valor in contatos.items():
 #   print(chave,valor)'''
print()
#--------------------------------------------------------
