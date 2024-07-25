from package_utils.validador import verifica_cpf_cadastrado, verifica_letras_operadores

# Lista o Extrato
def extrato(saldo, /,*, extrato=''):
    extrato_total = f'''   
- Extrato

{extrato}
- Saldo Total R$ {saldo:.2f}'''
    return print(extrato_total)
    
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
    cpf = input('Digite o CPF do usuário: ')
    if not verifica_letras_operadores(cpf):
        if verifica_cpf_cadastrado(cpf, lista_contas):
            print('Realizando consulta...')
            contas = [conta for conta in lista_contas if conta['CPF'] == cpf] # Verifica todas as contas do usuário
            for conta in contas:
                print_dic(**conta)
    else:
        print('O CPF deve conter apenas números!')
    

def print_dic(**kwargs): # Imprimi os dados do dicionário
    print('DADOS DO USUÁRIO:')
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')