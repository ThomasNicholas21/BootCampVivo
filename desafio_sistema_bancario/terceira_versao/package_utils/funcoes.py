from package_utils.classes import *

def menu():
    menu= '''
Menu de Opções:
[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastro de Usuário
[cc] Cadastro Conta
[lc] Listar contas
[q] Sair
Selecione:'''
    return menu

def filtro_cliente(cpf, clientes):
    filtro = [cliente for cliente in clientes if cliente.cpf == cpf]
    return filtro[0] if filtro else None

def filtro_conta(cliente):
    if not cliente.contas:
        print('Cliente sem conta!')
    return cliente.contas[0]

def depositar(clientes):
    cpf = input('Informe o CPF:')
    cliente = filtro_cliente(cpf, clientes)

    if not cliente:
        print('Cliente não encontrado!')
        return 
    
    valor = float(input("Insira a quantidade que será depositada: ")) 
    transacao = Deposito(valor)

    conta = filtro_conta(cliente)
    
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input('Informe seu CPF:')
    cliente = filtro_cliente(cpf, clientes)

    if not cliente:
        print('Cliente não encontrado!')
        return
    
    valor = float(input("Informe quanto deseja sacar: "))
    transacao = Saque(valor)

    conta = filtro_conta(cliente)

    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def extrato_usuario(clientes):
    cpf = input('Informe seu CPF:')

    cliente = filtro_cliente(cpf, clientes)
    if not cliente:
        print('Esse cliente não está cadastrado')
        return
    
    conta = filtro_conta(cliente)
    if not conta:
        print('Usuário não possui conta')
        return
    
    print('EXTRATO:')
    transacoes = conta.historico.transacoes

    extrato = ''
    if not transacoes:
        print('Nenhum movimento, sem historico de movimentacoes')
    else:
        for transacao in transacoes:
            extrato += f'\n{transacao['Tipo']}\nR${transacao['Valor']:.2f}'

    print(extrato)
    print(f'Saldo:R${conta.saldo:.2f}')
    
def cadastro_endereco(endereco={}):
    logradouro = input('Digite seu logradouro:')
    numero = input('Digite o número:')
    bairro = input('Digite seu bairro: ')
    cidade_estado = input('Digite sua Cidade/Estado(Sigla):')
    endereco.update({'Logradouro':logradouro, 'Numero': numero, 'Bairro': bairro, 'Cidade/Estado': cidade_estado})
    return endereco

def realizar_cadastro():
    realizar_cadastro = input('Desaja realizar o cadastro de uma conta? [S]im ou [N]ão:').lower().startswith('s')
    if realizar_cadastro:
        return True
    return False

def criar_usuario(clientes):
    cpf = input('Informe seu CPF:')
    cliente = filtro_cliente(cpf, clientes)

    if not cliente:
        if realizar_cadastro():
            print('Iniciando cadastro...')
            nome_usuario = input('Digite seu nome:')
            data_de_nascimento = input('Data de Nascimento:')

            print('**Cadastre seu Endereço**')
            endereco = {}
            cadastro_endereco(endereco)

            cliente = PessoaFisica(nome=nome_usuario, data_nascimento=data_de_nascimento, cpf=cpf, endereco=endereco)
            clientes.append(cliente)
            print('Cadastro Realizado com Sucesso.')
        
        else:
            print('Cadastro cancelado.')
            return

    else: 
        print('Usuário já possui cadastro.')
        return

def criar_conta(contas, clientes):
    cpf = input('Informe seu CPF:')
    cliente = filtro_cliente(cpf, clientes)

    if not cliente:
        print('Este usuário não é um cliente.')

    if realizar_cadastro():
        print('Criando conta...')
        contador = [cont for cont in contas if cliente.cpf == cpf ]
        numero_conta = len(contador) + 1
    
        conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
        cliente.contas.append(conta)
        print('Cadastro finalizado')

    else:
        print('Cadastro cancelado.')
        return

def listagem_conta(contas):
    for conta in contas:
        print(conta)
             