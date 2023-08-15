# Indentação em Python é feita por TAB (espaço e recuo do cursor)

def sacar(valor): # início do bloco do método
    if saldo >= valor: # início do bloco do if
        print("Valor sacado") 
        print("Retire o seu dinheiro do caixa!")
    # fim do bloco do if
    else:
        print("valor insuficiente")
    print("Obrigado por ser nosso cliente, tenha um bom dia!")
# fim do bloco do método

def depositar(valor):
    saldo = saldo + valor

saldo = int(input('Digite o valor que tem na conta: '))    
sacar(1000)
depositar(500)
sacar(1000)
#-----------------------------------------------------------------

