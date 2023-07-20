import textwrap

def menu():
    menu = f'''
{'='*20} MENU {'='*20}
[1]\tDepositar
[2]\tSacar
[3]\tExtrato
[4]\tNova Conta
[5]\tListar Contas
[6]\tfiltrar Contas
[7]\tNovo Usuário
[8]\tSair
==>  '''
    return input(textwrap.dedent(menu) )

def depositar(saldo, valor,extrato,/):
    if valor > 0:
        saldo = saldo + valor
        extrato = extrato + f'Depósito: R$: {valor:.2f}\n'
        print('\n=== Depósito realizado com sucesso" ===')

    else:
        print('\n@@@ Operação falhou! O valor informado é inválido. @@@')

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = valor > limite_saques

    if excedeu_saldo:
        print('\n@@@ Operação falho! Você não tem saldo suficiente. @@@')
    
    elif excedeu_limite:
        print('\n@@@ Operação falho! O valor do saque excede o limite. @@@')
        
    elif excedeu_saques:
        print('\n@@@ Operação falho! Número máximo de sauqes excedido. @@@')

    elif valor > 0:
        saldo = saldo - valor
        extrato = extrato + f'Saque:\t\tR$: {valor:.2f}\n'
        numero_saques = numero_saques + 1
        print('\n=== Saque realizado com sucesso! ===')
    
    else:
        print('\n@@@ Operação falhou. O valor informado é inválido. @@@')

    return saldo, extrato

def exebir_extrato(saldo, /, *, extrato):
     print(f'''
{'='*20} MENU {'='*20}
Não foram realizadas movimentações.'''if not extrato else extrato)
     print(f'''\nSaldo:\t\tR$: {saldo:.2f}
{'='*40}''')
     
def criar_usuario(usuarios): 
    cpf = input(('Informe o CPF (somente números): '))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n@@@ Já existe usuário com esse CPF! @@@')
        return
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço (logradouro, nro - bairro, cidade/sigla estado): ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print('=== Usuário criado com sucesso" ===')

def filtrar_usuario(cpf, usuarios):
    
def criar_conta(agencia, numero_conta, usuarios):

def listar_contas(contas):

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        
        if opcao == 1:
            valor = float(input('Informe o valor do depósito: '))

            saldo = depositar(saldo, valor, extrato)
            extrato = depositar(saldo, valor, extrato)
        elif opcao == 2:
            valor = float(input('Informe o valor de saque: '))

            saldo = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques
                limite_saques=LIMITE_SAQUES,
            )
            extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == 3:
            exebir_extrato(saldo, extrato = extrato)

        elif opcao == 4:
            criar_usuario(usuarios)

        elif opcao == 5:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == 6:
            listar_contas(contas)

        elif opcao == 7:
            break

        else:
            print('Opção inválida. Por favor, tente novamente')

main() 