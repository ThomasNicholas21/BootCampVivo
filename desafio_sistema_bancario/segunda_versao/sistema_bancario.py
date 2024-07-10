import os as o

def deposito_operacao(saldo, valor, extrato_funcao, /):
    # retona saldo e extrato
    ...
def saque_operacao(*, saldo, valor_extrato, limite_numero_saques):
    # retorna saldo e extrato
    ...
# retorna saldo e extrato
def extrato(saldo, /,*, extrato=''):
    extrato_total = f'''   
- Extrato

{extrato}
- Saldo Total R$ {saldo:.2f}'''
    return print(extrato_total)
    ...


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
extrato_total = ""
saldo = 0
deposito_cont = 0
saque_cont = 0 

while True:
    opcoes = input(menu).strip().lower()
    if opcoes == 'd':
        while deposito_cont < 1:
            try:
                deposito = float(input("Insira a quantidade que será depositada: ")) 
                if deposito < 1:
                    print("Valor insuficiente, tente novamente.")
                    voltar_deposito_menu = input("Pressione [V] para voltar e [C] para continuar:").lower().startswith('v')
                    if voltar_deposito_menu:
                        break
                else:
                    deposito_cont += 1
            except ValueError:
                print("Valor inválido, tente novamente.")           
        else:
            deposito_cont = 0
            saldo += deposito
            extrato_total += f'Depósito:R${deposito:.2f}\n'
            o.system("cls")
        
    elif opcoes == 's':
        if quantidade_saque == LIMITE_DIARIO:
            print("Quantidade de saque diário excedida. Tente amanhã.")
            continue
        while saque_cont < 1:
            try:
                saque = float(input("Informe quanto deseja sacar: "))
                if saque > 500:
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
            quantidade_saque += 1
            saldo -= saque
            extrato_total += f'Saque: R${saque:.2f}\n'    
            o.system("cls")

    elif opcoes == 'e':
        extrato(saldo, extrato=extrato_total)

    elif opcoes == 'q':
        print("Obrigado por utilizar nosso sistema!")
        break

    else:
        print("Opção inválida! Por gentileza, selecione uma das opções"
              "do menu.")
