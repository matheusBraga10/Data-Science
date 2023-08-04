def titulo(mensagem): 
    '''
    --> Imprime uma mensagem de título, com formatação padrão
    
    Função criada por Matheus Felipe Braga
    '''
    print('-'*30)
    print(mensagem)
    print('-'*30)


def menu():
    '''
    --> Imprime na tela um menu com as opções, pedindo para digitar a opção desejada
        - inputar um numero inteiro para a opção desejada
    
    Função criada por Matheus Felipe Braga
    '''
    titulo('   MENU PRINCIPAL   ')
    menu = print(f'''
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
    '''
    - Deposita valor na conta 
        - Todos os parâmetros deverão ser por posição
        - Pede para digitar um valor flutuante.
        - Se o valor for maior que 0: 
            - O valor será somado ao saldo. O valor também será somado ao extrato.
            - Caso contrário, retornará uma menságem de erro.
    - Deve retornar os valores salvos somados (saldo, extrato)
    
    Função criada por Matheus Felipe Braga
    '''
    
    if valor > 0:
        saldo = saldo + valor
        extrato = extrato + f'Depósito: R$ {valor:.2f}\n'
        titulo('   VALOR DEPOSITADO COM SUCESSO   ')
    else:
        titulo('~~~ ERRO. Valor inválido. Tente novamente. ~~~')
    
    return saldo, extrato


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    '''
    - Efetua saque 
        - Todos os parâmetros devem ser nomeados
        - Pede para entrar com o valor flutuante a ser sacado.
            - Se valor > saldo, programa aponta falha por exceder o saldo.
            - Se valor > limite, programa aponta falha por exceder limite.
            - Se numero de saques > limite de saques, programa aponta falha por exceder numero de saques diários.
            - Se valor > 0:
                - valor é subtraído no saldo.
                - extrato é subtraído do extrato.
                - numero de saques é somado com +1 a cada novo saque.
            - Se não, o programa deve apontar falha por valor inválido.
    - Retorna saldo e extrato.

    Função criada por Matheus Felipe Braga
    '''
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if valor > 0:
        saldo = saldo - valor
        numero_saques = numero_saques + 1
        limite = limite - valor
        extrato = extrato + f'Saque R$: {valor:.2f}\nLimite restante R$: {limite:.2f}\nNumero de saques diários restantes:  {limite_saques - numero_saques}\nSaldo em conta R$: {saldo:.2f}\n\n'
        titulo('  SAQUE REALIZADO COM SUCESSO.  ')
    elif excedeu_saldo:
        titulo('~~~ Falha. Saldo insuficiente. ~~~')
    elif excedeu_limite:
        titulo('~~~ Falha. O valor do saque excedeu o limite. ~~~')
    elif excedeu_saques:
        titulo('~~~ Falha. Você excedeu o número limite de saques diários. ~~~')
    else:
        titulo('~~~ Falha. Valor informado inválido. ~~~')

    return saldo, extrato


def imprime_extrato(saldo, /, *, extrato):
    '''
    - Imprime o extrato.
        - Se existir valor em extrato, imprimir o extrato
        - Se não, mostrar que não existem movimentações feitas.

    Função criada por Matheus Felipe Braga
    '''

    if extrato:
        titulo(extrato)
        
    else:
        titulo('~~~ Não existem movimentações em sua conta. ~~~')


def cria_usuario(usuarios):
    '''
    - Cria usuário:
        - Cadastra dados do usuário:
            - Pede string CPF.
                - Caso haja CPF igual já cadastrado, o programa retorna com mensagem de erro.
            - Pede string nome.
            -  Pede string data de nascimento.
            - Pede string endereço.
        - Cria um dicionário do usuário

    Função criada por Matheus Felipe Braga
    '''

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
    '''
    - Filtra usuário pelo CPF
        - Para cada usuário no banco de dados:
            - Se o CPF do usuário for igual
                - retorna o dicionário deste usuário
            - Se não, retorna nulo.

    Função criada por Matheus Felipe Braga
    '''
    filtro_de_usuarios = usuario['cpf']

    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return filtro_de_usuarios[0]
        else:
            return
    

def cria_conta(agencia, numero_conta, usuarios, contas):
    '''
    - Cria conta, com base nos dados do usuário cadastrado.
        - Pede a string CPF.
        - Filtra o CPF com base nos dados dos usários cadastrados.
        - Se existir o CPF no banco de dados
            - Imprime mensagem de conta criada
            - Retorna os dados adicionados no dicionário do usuário, para o usuário correto.
                - Agencia, numero da conta, usuário.
        - Se não
            - Imprime falha, usuário não encontrado.

    Função criada por Matheus Felipe Braga'''

    cpf = input('Informe o CPF (somente os números).\n==>  ')
    usuario = filtra_usuario(cpf, usuarios)

    if usuario:
        titulo('   CONTA CRIADA   ')
        return {'agencia':agencia, 'numero':numero_conta, 'usuario':usuario}
    
    titulo('~~~ Usuário não encontrado, faça o cadastro do usuário. ~~~')


def buscar_conta(usuario):
    '''
    - Realiza busca pela conta, com base no numero da conta
        - Se existir
            - Imprime numero da conta e demais dados do dicionário do usuário
        - Se não
            - Imprime mensagem de erro, conta não existe.

    Função criada por Matheus Felipe Braga
    '''
    conta = usuario.get(input('Digite o numero da conta do usuário desejado.\n==>  '))

    if conta:
        titulo(f'   CONTA ENCONTRADA   ')
        print(conta)
    else:
        titulo('~~~ Conta inexistente ~~~\n')
    

def main():
    '''
    - Roda opção para acesso a todas as funções criadas.
        - Enquanto as opções satisfazerem o programa 
            - Se a opção for 1, aciona a função deposito
            - Se a opção for 2, aciona a função extrato
            - Se a opção for 3, aciona a função cria usuário
            - Se a opção for 4, aciona a função saque
            - Se a opção for 5, aciona a função cria conta
            - Se a opção for 6, aciona a função busca conta
            - Se a opção for 7, sai do programa
            - Se a opção for outra, aciona uma mensagem de erro, como opção inválida

    Função criada por Matheus Felipe Braga
    '''
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
            titulo('   DEPOSITO   \n')
            valor = float(input('Informe o valor que deseja depositar.\n\n==>  '))
            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == 2:
            valor = float(input('Informe o valor que deseja sacar.\n\n==>  '))
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
            cria_conta()

        elif opcao == 6:
            buscar_conta()

        elif opcao == 7:
            titulo('   SAINDO DO PROGRAMA   ')
            break
        
        else:
            titulo('   OPÇÃO INVÁLIDA. TENTE NOVAMENTE!   ')


main()