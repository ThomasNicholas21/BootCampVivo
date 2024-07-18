import re

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
    while contador_deposito < 1:  # Inicia a operação deposito
            try:
                if deposito == 0: # Encerra a operação caso o usuário digite 0
                    print("❌ Operação Encerada ")
                    break
                else:   # Finaliza a repetição caso o usuário deseje realiar um depósito
                    contador_deposito += 1 
            except ValueError:
                print("Valor inválido, tente novamente.")           
    else: # Realiza a operação para inserção do depósito 
        saldo += deposito
        extrato_total += f'Depósito:R${deposito:.2f}\n'
        print("✔ Deposito Realizado ")
        return saldo, extrato_total
    
    return  saldo, extrato_total

# Realiza a Operação Saque
def saque_operacao(*, saldo, extrato_total): 
    saque_cont = 0
    while saque_cont < 1: # Inicia a operação Saque
            try: 
                saque = float(input("Informe quanto deseja sacar ou digite [0] para voltar: "))
                if saque == 0: # Regras de saque
                    print("❌ Operação Encerada ")
                    break
                elif saque > 500: # Regras de saque
                    print("Valor máximo de saque excedido, tente novamente.")
                elif saque > saldo: # Regras de saque
                    print(f"Saldo insuficiente, deposite e tente novamente.") 
                    break
                else: # Caso siga todas as regras sai da repetição
                    saque_cont += 1
            except ValueError: # Verifica se o usuário está inserindo outro valor além de número
                print("Valor inválido.")
    else: # Realiza a operação Saque
        saldo -= saque
        extrato_total += f'Saque: R${saque:.2f}\n' 
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
    cpf = input('Digite seu CPF:')
    if not verifica_letras_operadores(cpf): # Se não tiver letra e operadores inicia o cadastro
        if not verifica_cpf_cadastrado(cpf, lista_usuarios): # Verifica se o usuário não está cadastrado
            nome_usuario = input('Digite seu nome:')
            data_de_nascimento = input('Data de Nascimento:')
            print('**Cadastre seu Endereço**')
            logradouro = input('Digite seu logradouro:')
            numero = input('Digite o número:')
            bairro = input('Digite seu bairro: ')
            cidade_estado = input('Digite sua Cidade/Estado(Sigla):')
            lista_usuarios.append({"Nome":nome_usuario, "Data de Nascimento":data_de_nascimento, 
                                'CPF': cpf, 'endereço':{'logradouro':logradouro, 'numero': numero, 
                                                        'bairro': bairro, 'Cidade/Estado': cidade_estado}}) # Realiza a inserção de dados do cliente na lista de usuários
            print('✔ Usuário cadastrado com sucesso')
            return lista_usuarios
        else: # Caso o usuário já esteja cadastrado
            print('Erro, usuário já cadastrado')
            return lista_usuarios
    else:
        print('No CPF deve ser digitado apenas números')

def criar_conta(lista_conta_corrente, lista_usuarios):
    cpf = input('Digite seu CPF: ')
    if not verifica_letras_operadores(cpf):
        if verifica_cpf_cadastrado(cpf, lista_usuarios): # Verifica se tem usuários cadastrados
            criar = input('Deseja criar um conta, digite [s] para sim ou qualquer tecla para não: ').lower().startswith('s')
            if criar: # Inicia o processo de criação dascontas
                print('Criando conta...')
                contas = [conta for conta in lista_conta_corrente if conta['CPF'] == cpf] # Cria um nova lista que tem todas as contas criadas em um CPF
                n_conta = len(contas) + 1 # Faz a contagem de contas do usuário para que não haja números repetidos
                lista_conta_corrente.append({'Agênci-a': '0001', 'Número da Conta': n_conta, 'CPF': cpf}) # Inseri as informações da conta do usuário
                print('✔ Conta Criada com sucesso')
                return lista_conta_corrente
            else:
                print('Cancelando criação de conta ...')  
                return lista_conta_corrente        
        else:
            print('Este CPF é inválido')
            return lista_conta_corrente
    else:
        print('O CPF deve conter apenas números!')
        return lista_conta_corrente
    
# Lista o usuários cadastrados
def lista_usuarios(lista_de_dados):
    lista = {}
    cpf = input('Digite o CPF do usuário: ')
    if not verifica_letras_operadores(cpf): 
        print('Realizando consulta...')
        if verifica_cpf_cadastrado(cpf, lista_de_dados): # Verifica se o usuário está cadastrado
            for valores in lista_de_dados: 
                if valores['CPF'] == cpf:  # Procura pelo usuário
                    for chave, valor in valores.items(): # Inseri em um dicionário
                        lista.setdefault(chave, valor)   
            return print_dic(**lista)
        return print('Usuário não encontrado!')
    else:
        return print('O CPF deve conter apenas números!')

# Lista contas
def lista_contas(lista_contas):
    lista = {}
    cpf = input('Digite o CPF do usuário: ')
    if not verifica_letras_operadores(cpf):
        if verifica_letras_operadores(cpf): # Verifica se o usuário existe
            print('Realizando consulta...')
            if not verifica_cpf_cadastrado(cpf, lista_contas):
                contas = [conta for conta in lista_contas if conta['CPF'] == cpf] # Verifica todas as contas do usuário
                for conta in contas:
                    print_dic(**conta, sep='\n')
    else:
        return print('O CPF deve conter apenas números!')

def verifica_letras_operadores(cpf): # Função de validação de operadores e letra
    validacao = r"[a-zA-Z+\-*/]"
    return bool(re.search(validacao, cpf)) # Retorna True se letras e operadores estiverem presentes
    
def verifica_cpf_cadastrado(cpf, lista_de_dados): # Valida se o CPF está cadastrado
    for dados in lista_de_dados:
        if dados['CPF'] == cpf:
            return True
    return False

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
            if quantidade_saque >= 3: # Caso o usuário tenha realizado 3 vezes, a operação é bloqueda
                print("Quantidade de saque diário excedida. Tente amanhã.")
            else:
                saldo, extrato_total = saque_operacao(saldo=saldo, extrato_total=extrato_total)
                quantidade_saque += 1

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