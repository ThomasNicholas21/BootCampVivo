from package_utils import deposito_operacao, saque_operacao, extrato, cadastro_usuario, criar_conta, lista_usuarios, lista_contas

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

def main():
    lista_de_conta_corrente = []
    lista_de_usuario = []
    quantidade_saque = 0
    extrato_total = ""
    saldo = 0
    opcoes = ''

    while True:
        opcoes = input(menu()).lower().strip() # Chama a função menu para o usuário selecionar qual a opção desejada
        if opcoes == 'd': # Caso o usuário deseje depositar
            deposito = float(input("Insira a quantidade que será depositada ou digite [0] para voltar: ")) 
            saldo, extrato_total = deposito_operacao(saldo, deposito, extrato_total)
            
        elif opcoes == 's': # Caso o usuário deseje sacar
            if quantidade_saque >= 3: # Caso o usuário tenha realizado 3 vezes, a operação é bloqueda
                print("Quantidade de saque diário excedida. Tente amanhã.")
            else:
                saldo, extrato_total = saque_operacao(saldo=saldo, extrato_total=extrato_total)
                quantidade_saque += 1

        elif opcoes == 'e': # Caso o usuário deseje visualizar o extrato
            extrato(saldo, extrato=extrato_total)
        
        elif opcoes == 'c': # Caso o usuário deseje cadastrar um usuário
            lista_de_usuario = cadastro_usuario(lista_de_usuario)
        
        elif opcoes == 'ccc': # Caso o usuário deseje criar um contato corrente
            lista_de_conta_corrente = criar_conta(lista_de_conta_corrente, lista_de_usuario)
        
        elif opcoes == 'lu': # Caso o usuário deseje listar os dados de um usuário especifico
            lista_usuarios(lista_de_usuario)
        
        elif opcoes == 'lc': # Caso o usuário deseje listar contas especificas
            lista_contas(lista_de_conta_corrente)

        elif opcoes == 'q': # Caso o usuário deseje encerrar o programa
            print("Obrigado por utilizar nosso sistema!")
            break

        else: # Caso o usuário erre o menu
            print("Opção inválida! Por gentileza, selecione uma das opções"
                "do menu.")
                   
main()