def menu():
    menu= '''
Menu de Opções:
[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastro de Usuário
[ccc] Criar Conta Corrente
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

def valida_cpf(cpf, lista_de_usuario):
    for dados in lista_de_usuario:
        for dado in dados.values():
            if dado == cpf:
                return False
    return True
    
def cadastro_usuario(lista_usuarios):
    try:
        cpf = input('Digite seu CPF:')
        print(valida_cpf(cpf, lista_usuarios))
        if valida_cpf(cpf, lista_usuarios):
            nome_usuario = input('Digite seu nome:')
            data_de_nascimento = input('Data de Nascimento:')
            print('Cadastre seu Endereço:')
            logradouro = input('Digite seu logradouro:')
            numero = input('Digite o número:')
            bairro = input('Digite seu bairro: ')
            cidade_estado = input('Digite sua Cidade/Estado(Sigla):')
            lista_usuarios.append({"Nome":nome_usuario, "Data de Nascimento":data_de_nascimento, 
                                'CPF': cpf, 'endereço':{'logradouro':logradouro, 'numero': numero, 
                                                        'bairro': bairro, 'Cidade/Estado': cidade_estado}})
            return lista_usuarios
        else:
            print('Erro, usuário já cadastrado')
            return lista_usuarios
    except:
        print('No CPF deve ser digitado apenas números')

def criar_conta():
    ...
  
def main():
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
            print(lista_de_usuario)

        elif opcoes == 'q':
            print("Obrigado por utilizar nosso sistema!")
            break

        else:
            print("Opção inválida! Por gentileza, selecione uma das opções"
                "do menu.")
                   
main()