def menu():
    menu= '''
Menu de Opções:
[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastro de Usuário
[ccc] Criar Conta Corrente
[lu] Listar usuários
[lc] Listar usuários
[q] Sair
Selecione:'''
    return menu

# Realiza Operação Deposito
def deposito_operacao(saldo, deposito, extrato_total, /):
    contador_deposito = 0   
    while contador_deposito < 1:
            try:
                if deposito == 0:
                    print("❌ Operação Encerada ")
                    break
                else:
                    contador_deposito += 1
            except ValueError:
                print("Valor inválido, tente novamente.")           
    else:
        contador_deposito = 0
        saldo += deposito
        extrato_total += f'Depósito:R${deposito:.2f}\n'
        print("✔ Deposito Realizado ")
        return saldo, extrato_total
    
    return  saldo, extrato_total

# Realiza a Operação Saque
def saque_operacao(*, saldo, extrato_total, quantidade_saque): 
    saque_cont = 0
    while saque_cont < 1:
            if quantidade_saque >= 3:
                print("Quantidade de saque diário excedida. Tente amanhã.")
                return  saldo, extrato_total
            try:
                saque = float(input("Informe quanto deseja sacar ou digite [0] para voltar: "))
                if saque == 0:
                    print("❌ Operação Encerada ")
                    break
                elif saque > 500:
                    print("Valor máximo de saque excedido, tente novamente.")
                elif saque > saldo:
                    print(f"Saldo insuficiente, deposite e tente novamente.") 
                    break
                else:
                    saque_cont += 1
            except ValueError:
                print("Valor inválido.")
    else:
        saque_cont = 0 
        saldo -= saque
        extrato_total += f'Saque: R${saque:.2f}\n' 
        quantidade_saque += 1
        print("✔ Saque Realizado ")
        return  saldo, extrato_total
    
    return  saldo, extrato_total

# Lista o Extrato
def extrato(saldo, /,*, extrato=''):
    extrato_total = f'''   
- Extrato

{extrato}
- Saldo Total R$ {saldo:.2f}'''
    return print(extrato_total)

# Realiza Cadastro de Usuário
def cadastro_usuario(lista_usuarios):
    try:
        cpf = input('Digite seu CPF:')
        if verifica_cpf_cadastrado(cpf, lista_usuarios):
            nome_usuario = input('Digite seu nome:')
            data_de_nascimento = input('Data de Nascimento:')
            print('**Cadastre seu Endereço**')
            logradouro = input('Digite seu logradouro:')
            numero = input('Digite o número:')
            bairro = input('Digite seu bairro: ')
            cidade_estado = input('Digite sua Cidade/Estado(Sigla):')
            lista_usuarios.append({"Nome":nome_usuario, "Data de Nascimento":data_de_nascimento, 
                                'CPF': cpf, 'endereço':{'logradouro':logradouro, 'numero': numero, 
                                                        'bairro': bairro, 'Cidade/Estado': cidade_estado}})
            print('✔ Usuário cadastrado com sucesso')
            return lista_usuarios
        else:
            print('Erro, usuário já cadastrado')
            return lista_usuarios
    except:
        print('No CPF deve ser digitado apenas números')

def criar_conta(lista_conta_corrente, lista_usuarios):
    cpf = input('Digite seu CPF: ')
    if not verifica_cpf_cadastrado(cpf, lista_usuarios):
        criar = input('Deseja criar, digite [s] para sim ou [n] para não: ').lower().startswith('s')
        if criar:
            print('Criando conta...')
            contas = [conta for conta in lista_conta_corrente if conta['CPF'] == cpf]
            n_conta = len(contas) + 1
            lista_conta_corrente.append({'Agência': '0001', 'Número da Conta': n_conta, 'CPF': cpf})
            print('✔ Conta Criada com sucesso')
            return lista_conta_corrente
        else:
            print('Cancelando criação de conta ...')  
            return lista_conta_corrente        
    else:
        print('Este CPF é inválido')
        return lista_conta_corrente
    
def lista_usuarios(lista_de_dados):
    lista = {}
    cpf = input('Digite o CPF do usuário: ')
    print('Realizando consulta...')
    if not verifica_cpf_cadastrado(cpf, lista_de_dados):
        for valores in lista_de_dados:
            if valores['CPF'] == cpf: 
                for chave, valor in valores.items():
                    lista.setdefault(chave, valor)   
        return print_dic(**lista)
    return print('Usuário não encontrado!')

def lista_contas(lista_contas):
    lista = {}
    cpf = input('Digite o CPF do usuário: ')
    print('Realizando consulta...')
    if not verifica_cpf_cadastrado(cpf, lista_contas):
        contas = [conta for conta in lista_contas if conta['CPF'] == cpf]
        for conta in contas:
            print_dic(**conta, sep='\n')
    
def verifica_cpf_cadastrado(cpf, lista_de_dados):
    for dados in lista_de_dados:
        if dados['CPF'] == cpf:
            return False
    return True

def print_dic(**kwargs):
    print('DADOS DO USUÁRIO:')
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')
 
def main():
    lista_de_conta_corrente = []
    lista_de_usuario = []
    quantidade_saque = 0
    extrato_total = ""
    saldo = 0
    opcoes = ''

    while True:
        opcoes = input(menu()).lower().strip()
        if opcoes == 'd':
            deposito = float(input("Insira a quantidade que será depositada ou digite [0] para voltar: ")) 
            saldo, extrato_total = deposito_operacao(saldo, deposito, extrato_total)
            
        elif opcoes == 's':
            saldo, extrato_total = saque_operacao(saldo=saldo, extrato_total=extrato_total, quantidade_saque=quantidade_saque)

        elif opcoes == 'e':
            extrato(saldo, extrato=extrato_total)
        
        elif opcoes == 'c':
            lista_de_usuario = cadastro_usuario(lista_de_usuario)
        
        elif opcoes == 'ccc':
            lista_de_conta_corrente = criar_conta(lista_de_conta_corrente, lista_de_usuario)
        
        elif opcoes == 'lu':
            lista_usuarios(lista_de_usuario)
        
        elif opcoes == 'lc':
            lista_contas(lista_de_conta_corrente)

        elif opcoes == 'q':
            print("Obrigado por utilizar nosso sistema!")
            break

        else:
            print("Opção inválida! Por gentileza, selecione uma das opções"
                "do menu.")
                   
main()