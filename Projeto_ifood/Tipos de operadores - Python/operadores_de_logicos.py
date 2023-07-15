saldo = 1000
saque = 200
limite = 100

print(saldo >= saque and saque <= limite) 
# Condição de "and" para "True" é somente se o conjunto de expressões for verdadeiro

print(saldo >= saque or saque <= limite) 
# Condição de "or" para "True" é pelomenos uma expressão do conjunto for verdadeira

print(not saldo > saque) 
# Condição de "not" para "True" é uma expressão for falsa (contraria)
print(not saque <= limite) 
# Condição de "not" para "True" é uma expressão for falsa (contraria)

conta_especial = True
print(saldo >= saque and saque <= limite or conta_especial and saldo >= saque)
print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))

print(True and True)
print(True and False)
print(True or True)
print(True or False)
# and = para ser True, tudo tem que ser True
# or = para ser True, basta 1 ser True
