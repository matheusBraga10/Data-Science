# Desafio - Otimizando o Sistema Bancário com Funções Python

def deposito(valor):
    print('[1] - Deposito\n')
    
    if valor > 0:
        saldo = saldo + valor
        extrato = extrato + f'Depósito R$: {valor:.2f}\n\n'
        print(f'Seu depósito de R$:{valor:.2f} foi realizado com sucesso.')
    else:
        print('O valor não pode ser efetuado. Por favor, tente novamente.')

def saque():

def extrato():

def cadastro_usuario():

def cadastro_conta_bancaria():


menu = f'''
{'='*20}

[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Sair

{'='*20}
'''
saldo = 0
limite = 500
numero_de_saques = 0
LIMITE_DE_SAQUES = 3
extrato = f'''

{'='*20}
EXTRATO
{'='*20}

'''
while True:

    opcao = input(f'{menu}\n Opção: ')

    if opcao == '1':
        valor = float(input('\nQual o valor deseja depositar na conta? '))
        
    elif opcao == '2':
        print('[2] - Saque\n')
        while numero_de_saques < LIMITE_DE_SAQUES and saldo > 0:
            saque = float(input('Digite o valor que deseja sacar: R$: '))
            if limite >= saque:
                numero_de_saques = numero_de_saques + 1
                limite = limite - saque
                saldo = saldo - saque
                extrato = extrato + f'Saque R$: {saque:.2f}\nLimite restante R$: {limite:.2f}\nNumero de saques diários restantes:  {LIMITE_DE_SAQUES - numero_de_saques}\nSaldo em conta R$: {saldo:.2f}\n\n'
                print(f'''Saque de R$:{saque:.2f} efetuado com sucesso. Retire seu dinheiro.
                      Seu saldo foi atualizado para R$:{saldo:.2f} .
                      ''')
                break
            else:
                print('Você chegou ao limite de saques por dia, ou ultrapassou seu limite de crédito.')
                break
    elif opcao == '3':
        extrato = extrato + f'Saldo atual: R$:{saldo:.2f}\n'
        print(extrato)
        
    elif opcao == '4':
        print('[4] - Sair')
        break
    else:
        print('Opção inválida, tente novamente')
