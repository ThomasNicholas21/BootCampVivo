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