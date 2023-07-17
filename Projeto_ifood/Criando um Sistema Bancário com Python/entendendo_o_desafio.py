'''Fomos contratados por um grande banco para
desenvolver o seu novo sistema. Esse banco deseja
modernizar suas operações e para isso escolheu a 
linguagem Python. Para a primeira versão do sistema
devemos umplementar apenas 3 operações:

- Depósito
- Saque
- Extrato
'''
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
extrato = f'''[3] - Extrato

Seu saldo atual é de: R$:{saldo:.2f} .
Seu limite atual é de: R${limite:.2f} .
Você ainda tem direito de realizar mais {numero_de_saques} saques.'''
while True:

    opcao = input(f'{menu}\n Opção: ')

    if opcao == '1':
        print('[1] - Deposito\n')
        valor = float(input('\nQual o valor deseja depositar na conta? '))
        if valor > 0:
            saldo = saldo + valor
            print(f'Seu depósito de R$:{valor:.2f} foi realizado com sucesso.')
        else:
            print('O valor não pode ser efetuado. Por favor, tente novamente.')

    elif opcao == '2':
        print('[2] - Saque\n')
        while numero_de_saques < LIMITE_DE_SAQUES and saldo > 0:
            saque = float(input('Digite o valor que deseja sacar: R$: '))
            if limite >= saque:
                numero_de_saques = numero_de_saques + 1
                limite = limite - saque
                saldo = saldo - saque
                print(f'''Saque de R$:{saque:.2f} efetuado com sucesso. Retire seu dinheiro.
                      Seu saldo foi atualizado para R$:{saldo:.2f} .
                      ''')
                break
            else:
                print('Você chegou ao limite de saques por dia, ou ultrapassou seu limite de crédito.')
                break
    elif opcao == '3':
        print(extrato)
        
    elif opcao == '4':
        print('[4] - Sair')
        break
    else:
        print('Opção inválida, tente novamente')
