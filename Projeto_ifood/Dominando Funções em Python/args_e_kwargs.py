# *args - Tupla

# **kwargs - Dicionário

def exibir_poema(data_extenso, *tupla, **dicionario): #*args, **kwargs):
    texto = '\n'.join(tupla)
    meta_dados = '\n'.join([f'{chave.title()}: {valor}' for chave, valor in dicionario.items()])
    mensagem = f'{data_extenso}\n\n{texto}\n\n{meta_dados}'
    print(mensagem)

exibir_poema('18 de jul de 2023','Zen of Python','Beautiful is better than ugly.', autor='Tim Peters', ano=1999)
