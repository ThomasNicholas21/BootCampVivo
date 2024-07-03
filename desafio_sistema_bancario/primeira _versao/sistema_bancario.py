menu= '''
Menu de Opções:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
Selecione:'''

LIMITE_DIARIO = 3
quantidade_saque = 0
limite_saque = 500
extrato = ""
saldo = 0
deposito_cont = 0

while True:
    opcoes = input(menu).strip().lower()
    if opcoes == 'd':
        while deposito_cont < 1:
            try:
                deposito = float(input("Insira a quantidade que será depositada: ")) 
                if deposito < 1:
                    print("Valor insuficiente, tente novamente.")
                else:
                    deposito_cont += 1
            except ValueError:
                print("Valor inválido, tente novamente.")           
        else:
            deposito_cont = 0
            saldo += deposito
            extrato += f'Depósito: R${deposito:.2f}\n'
        
    elif opcoes == 's':
        try:
            saque = float(input("Informe quanto deseja sacar: "))
            if saque > 500:
                print("Valor máximo de saque excedido, tente novamente.")
            elif saque > saldo:
                print(f"Saldo insuficiente, não será possível sacar essa quantida.") 
            elif LIMITE_DIARIO == 0:
                print("Quantidade de saque diário excedida. Tente amanhã.")
            else:
                LIMITE_DIARIO -= 1
                saldo -= saque
                extrato += f'Saque: R${saque:.2f}\n'
        except ValueError:
            print("Valor inválido.")

    elif opcoes == 'e':
        print("\nExtrato atual:")
        print(extrato)
        print(f"Saldo atual: R${saldo:.2f}")

    elif opcoes == 'q':
        print("Obrigado por utilizar nosso sistema!")
        break

    else:
        print("Opção inválida! Por gentileza, selecione uma das opções"
              "do menu.")