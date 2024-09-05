from package_utils import menu, depositar, sacar, extrato_usuario, criar_usuario, criar_conta, listagem_conta

def main():
    clientes = []
    contas = []

    while True:
        opcoes = input(menu()).lower().strip() 
        if opcoes == 'd': 
            depositar(clientes)
            
        elif opcoes == 's':
            sacar(clientes)

        elif opcoes == 'e': 
            extrato_usuario(clientes)
        
        elif opcoes == 'c':
            criar_usuario(clientes)
        
        elif opcoes == 'cc':
            criar_conta(contas, clientes)
        
        elif opcoes == 'lc': 
            print(*clientes, sep='\n')
            listagem_conta(contas)

        elif opcoes == 'q':
            print("Obrigado por utilizar nosso sistema!")
            break

        else: 
            print("Opção inválida! Por gentileza, selecione uma das opções"
                "do menu.")
            
main()