# CONVERTENDO TIPOS

preco = 10
print(preco)

print(type(preco))

# Inteiros para Reais (flutuantes)
preco = float(preco)
print(preco)

print(type(preco))

# Reais (flutuantes) para Inteiros
preco = 10.2
print(preco)
preco = int(preco)
print(preco)

print(type(preco))

# Numero(inteiro ou flutuante) para String
preco = 10.5
idade = 28

print(str(preco))
print(str(idade))

print(type(idade))
print(type(preco))

# Concatenando String com Variáveis
texto = f'idade {idade} preco {preco}'
print(texto)

# String para Numeros(inteiros e flutuantes)
preco = '10.5'
idade = '28'

print(float(preco))
print(int(idade))

print(type(idade))
print(type(preco))
