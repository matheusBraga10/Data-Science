# *args - Tupla

# **kwargs - Dicionário

def exibir_poema(data_extenso, *tupla, **dicionario): #*args, **kwargs):
    texto = '\n'.join(tupla)
    meta_dados = '\n'.join([f'{chave.title()}: {valor}' for chave, valor in dicionario.items()]) 
    ''' meta_dados : É uma junção de dicionários descritos abaixo: 

        - .join(tupla) : .join faz uma junção das tuplas declaradas na função 'exibir_poema'
        - for chave, valor in dicionario.items() : 'items' retorna lista de tuplas dentro do 'dicionario' que são 'chave' e 'valor', para o 'for' iterar
    '''
    mensagem = f'{data_extenso}\n\n{texto}\n\n{meta_dados}'
    print(mensagem)

exibir_poema('18 de jul de 2023','Zen of Python','Beautiful is better than ugly.', autor='Tim Peters', ano=1999)
