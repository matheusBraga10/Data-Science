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
{=*20}

[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Sair

{=*20}
'''
saldo = 0
limite = 500
extrato = f''''''
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:

    opcao = input(f'{menu}\n Opção: ')

    if opcao == '1':
        print('[1] - Deposito')
        
    
    elif opcao == '2':
        print('[2] - Saque')
        
    elif opcao == '3':
        print('[3] - Extrato')
        
    elif opcao == '4'
        print('[4] - Sair')
        break
    else:
        print('Opção inválida, tente novamente')