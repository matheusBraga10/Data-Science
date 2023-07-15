saldo = 2000
saque = float(input('Informe o valor do saque: '))

if saldo >= saque:
    print('Realizando saque!')
else:
    print('Saque insuficiente!')

#------------------------------------------------------------------
opcao = int(input('Informe uma opção: \n[1] Saque\n[2] Extrato\nOpção: '))

if opcao == 1:
    valor = float(input('Informe a quantia para o saque: '))
elif opcao == 2:
    print('Exibindo o extrato...')
else:
    exit('Opção invalida')

#------------------------------------------------------------------
MAIOR_IDADE =  18

idade  = int(input('Informe sua idade: '))

if idade >= MAIOR_IDADE:
    print('Maior de idade, pode tirar CNH.')
else:
    print('Ainda não pode tirar a CNH.')

#-------------------------------------------------------------------
# Estrutura condicional ternária
saldo = 2000
saque = 500

status = 'Sucesso' if saldo >= saque else 'Falha'
print((f'`{status} ao realizar o saque!'))
