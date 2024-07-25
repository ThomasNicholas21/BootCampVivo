from package_utils.validador import verifica_cpf_cadastrado, verifica_letras_operadores

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
                lista_conta_corrente.append({'Agência': '0001', 'Número da Conta': n_conta, 'CPF': cpf}) # Inseri as informações da conta do usuário
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