# Métodos da Classe Dict (Dicionários)

contatos = {
    '001': {'nome':'Matheus','idade':34},
    '002': {'nome':'Maria','idade':32},
    '003': {'nome':'Ana','idade':31},
    '004': {'nome':'João','idade':37}
}
print(contatos)
print()
#-------------------------------------------
#{}.clear - limpa todos os dados
# contatos.clear()
# print(contatos)
print()
#-------------------------------------------
#{}.copy - copia todos os dados para outro dicionario de mesmo nome
copia = contatos.copy()
print(copia)
print()
#-------------------------------------------
#{}.fromkeys
dict.fromkeys(['name','phone'])

copia.fromkeys(['name','phone'],'vazio')
print(copia)
print()
#-------------------------------------------
#{}.get - Para quando não sabemos se existe ou não uma chave
print(contatos.get('005')) # None (chave inexistente)
print(contatos.get('005', 'Chave_INEXISTENTE')) # Chave_INEXISTENTE (chave inexistente)
print(contatos.get('004'))

print()
#-------------------------------------------
#{}.items - Retorna lista de tuplas para ser posséível iterar
contatos.items()
print(contatos)
print()
#-------------------------------------------
#{}.keys - Retorna somente as chaves
print(contatos.keys())
print()
#-------------------------------------------
#{}.pop - Remove uma chave do dicionario
contatos.pop('004')
print(contatos)
print()
#-------------------------------------------
#{}.popitem - Remove a ultima chave do dicionario
contatos.popitem()
print(contatos)
print()
#-------------------------------------------
#{}.setdefault - Não altera dados, caso tenha a chave, porém, adiciona chaves que não existem, com dados novos
contato = {'nome','Guilherme','telefone','3333-2222'}
#contato.setdefault('nome','Jorge')
#contato.setdefault('idade', 53)
print(contato)
print()
#-------------------------------------------
#{}.update - Atualiza o dicionario com outro
contatos.update({'005':{'nome':'Gui'}})
print(contatos)
print()
#-------------------------------------------
#{}.values - Retorna todos os valores
print(contatos.values())
print()
#-------------------------------------------
#in
resultado = 'idade' in contatos['001']
print(resultado)
print('telefone' in contatos['001'])
print()
#-------------------------------------------
#del - Remove ou deleta dados
del contatos['002']
print(contatos)
del contatos['001']['nome']
print(contatos)

