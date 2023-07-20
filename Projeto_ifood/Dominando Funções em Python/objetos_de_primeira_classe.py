def somar(a,b):
    return a+b

def subtrair(a,b):
    return a-b

def exibir_resultado(a,b,funcao):
    resultado = funcao(a,b)
    print(f'O resultado da operação é de {resultado}')

exibir_resultado(10,10, somar) # Resultado da operação 10 + 10 = 20
exibir_resultado(10,10, subtrair)

op = somar
print(op(1,23))