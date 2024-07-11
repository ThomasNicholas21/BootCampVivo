import os as o

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


def menu():
    menu= '''
Menu de Opções:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
Selecione:'''
    return menu
    
def main():
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

        elif opcoes == 'q':
            print("Obrigado por utilizar nosso sistema!")
            break

        else:
            print("Opção inválida! Por gentileza, selecione uma das opções"
                "do menu.")
                   
main()