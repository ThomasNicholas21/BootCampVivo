from package_utils import menu, depositar, sacar, extrato_usuario, criar_usuario, criar_conta, listagem_conta

def main():
    clientes = []
    contas = []

    while True:
        opcoes = input(menu()).lower().strip() # Chama a função menu para o usuário selecionar qual a opção desejada
        if opcoes == 'd': # Caso o usuário deseje depositar
            depositar(clientes)
            
        elif opcoes == 's': # Caso o usuário deseje sacar
            sacar(clientes)

        elif opcoes == 'e': # Caso o usuário deseje visualizar o extrato
            extrato_usuario(clientes)
        
        elif opcoes == 'c': # Caso o usuário deseje cadastrar um usuário
            criar_usuario(clientes)
        
        elif opcoes == 'cc': # Caso o usuário deseje criar um contato corrente
            criar_conta(contas, clientes)
        
        elif opcoes == 'lc': # Caso o usuário deseje listar os dados de um usuário especifico
            print(*clientes, sep='\n')
            listagem_conta(contas)

        elif opcoes == 'q': # Caso o usuário deseje encerrar o programa
            print("Obrigado por utilizar nosso sistema!")
            break

        else: # Caso o usuário erre o menu
            print("Opção inválida! Por gentileza, selecione uma das opções"
                "do menu.")
            
main()