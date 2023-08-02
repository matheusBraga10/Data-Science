def titulo(mensagem): 
    '''
    --> Imprime uma mensagem de título, com formatação padrão
    
    Função criada por Matheus Felipe Braga
    '''
    print('-'*30)
    print(mensagem)
    print('-'*30)


def menu():
    titulo('   MENU PRINCIPAL   ')
    print(f'''
[1] - DEPOSITO
[2] - SAQUE
[3] - EXTRATO
[4] - NOVA CONTA
[5] - NOVO USUÁRIO
[6] - BUSCAR CONTA
[7] - SAIR

INFORME A OPÇÃO DESEJADA ==>  ''')
    return int(input(menu))


def deposito(saldo, valor, extrato, /):
    valor = float(input('Informe o valor que deseja depositar.\n\n==>  '))
    if valor > 0:
        saldo = saldo + valor
        extrato = extrato + f'Depósito: R$ {valor:.2f}\n'
        titulo('   VALOR DEPOSITADO COM SUCESSO   ')
    else:
        titulo('~~~ ERRO. Valor inválido. Tente novamente. ~~~')
    
    return saldo, extrato


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    valor = float(input('Informe o valor que deseja sacar.\n\n==>  '))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques - 1

    if excedeu_saldo:
        titulo('~~~ Falha. Saldo insuficiente. ~~~')
    elif excedeu_limite:
        titulo('~~~ Falha. O valor do saque excedeu o limite. ~~~')
    elif excedeu_saques:
        titulo('~~~ Falha. Você excedeu o número limite de saques diários. ~~~')
    elif valor > 0:
        saldo = saldo + valor
        extrato = extrato + f'Depósito: R$ {valor:.2f}\n'
        numero_saques = numero_saques + 1
        titulo('  SAQUE REALIZADO COM SUCESSO.  ')
    else:
        titulo('~~~ Falha. Valor informado inválido. ~~~')

    return saldo, extrato


def imprime_extrato(saldo, /, *, extrato):
    if not extrato:
        titulo('~~~ Não existem movimentações em sua conta. ~~~')
    else:
        titulo(f'   Saldo: R$ {saldo:.2f}.   ')


def cria_usuario(usuarios):
    cpf = input('Informe o CPF (somente os números).\n==>  ')
    usuario = filtra_usuario(cpf, usuario)

    if usuario:
        titulo('~~~ Este CPF já possui cadastro. ~~~')
        return
    nome = input(' Informe o nome completo.\n==>  ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa).\n==>  ')
    endereco = logradouro + bairro + cidade
    logradouro = input('Informe logradouro (rua, n°/complemento).\n==>  ')
    bairro = input('Informe seu bairro.\n==>  ')
    cidade = input('Informe sua cidade e estado (Cidade/Sigla estado).\n==>  ')

    usuario.append({'cpf':cpf, 'nome':nome, 'data_nascimento': data_nascimento, 'endereco':endereco})
    titulo('   USUÁRIO CRIADO COM SUCESSO.   ')


def filtra_usuario(cpf, usuarios):
    filtro_de_usuarios = usuario['cpf']

    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return filtro_de_usuarios[0]
        else:
            return None
    

def cria_conta(agencia, numero_conta, usuarios, contas):
    cpf = input('Informe o CPF (somente os números).\n==>  ')
    usuario = filtra_usuario(cpf, usuarios)

    if usuario:
        titulo('   CONTA CRIADA   ')
        return {'agencia':agencia, 'numero':numero_conta, 'usuario':usuario}
    
    titulo('~~~ Usuário nã encontrado, faça o cadastro do usuário. ~~~')


def buscar_conta():
    

def dados():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []


def main():
    dados()
    while True:
        opcao = menu()

        if opcao == 1:
            titulo('   DEPOSITO   \n')
            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == 2:
            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == 3:
            imprime_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            cria_usuario(usuarios)

        elif opcao == 5:
            cria_conta(AGENCIA, numero_conta, usuarios, contas)


        elif opcao == 6:
            buscar_conta()


        elif opcao == 7:
            titulo('   SAINDO DO PROGRAMA   ')
            break

        else:
            titulo('   OPÇÃO INVÁLIDA. TENTE NOVAMENTE!   ')

