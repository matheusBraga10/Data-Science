def carro(marca, modelo, ano, placa):
    # Salva dados no banco de dados
    print(f'Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}')

# carro('Fiat','Palio',1999,'ABC-1234')
# carro(marca='Fiat',modelo='Palio',ano=1999,placa='ABC-1234') #(MELHOR SEGURANÇA COM O ARGUMENTO NOMEADO)
carro(**{'marca':'Fiat','modelo':'Palio','ano':1999,'placa':'ABC-1234'}) #(MODELO JÁ SALVO EM UM DICIONÁRIO)

print(carro)

