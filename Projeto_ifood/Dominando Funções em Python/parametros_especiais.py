# Parâmetros nomeados e por preposição

def carro(modelo, ano, placa,/,marca,motor,combustivel):
    print(modelo,ano,placa,marca,motor,combustivel)

carro('Palio',1999,'ABC-1234',marca='Fiat',motor='1.0',combustivel='Gasolina') # Válido

# carro('Palio',1999,'ABC-1234','Fiat','1.0','Gasolina') # Válido

# carro(modelo='Palio',ano=1999,placa='ABC-1234',marca='Fiat',motor='1.0',combustivel='Gasolina') # Inválido
print()
#-------------------------------------------------------------------------------------------------------------
# Parâmetros nomeados

def carro(*,modelo, ano, placa,marca,motor,combustivel):
    print(modelo,ano,placa,marca,motor,combustivel)

carro(modelo='Palio',ano=1999,placa='ABC-1234',marca='Fiat',motor='1.0',combustivel='Gasolina') # Válido

# carro('Palio',1999,'ABC-1234',marca='Fiat',motor='1.0',combustivel='Gasolina') # Inválido

# carro('Palio',1999,'ABC-1234','Fiat','1.0','Gasolina') # Inválido

print()
#-------------------------------------------------------------------------------------------------------------
# Parâmetros híbrido
def carro(modelo, ano, placa,/,marca,*,motor,combustivel):
    print(modelo,ano,placa,marca,motor,combustivel)

carro('Palio',1999,'ABC-1234',marca='Fiat',motor='1.0',combustivel='Gasolina') # Válido

# carro('Palio',1999,'ABC-1234','Fiat',motor='1.0',combustivel='Gasolina') # Válido
