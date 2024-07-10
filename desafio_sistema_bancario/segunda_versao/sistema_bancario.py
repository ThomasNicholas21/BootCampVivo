import os as o

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

saque_cont = 0 

while True:
    opcoes = input(menu).strip().lower()
    if opcoes == 'd':
        deposito = float(input("Insira a quantidade que será depositada ou digite [0] para voltar: ")) 
        saldo, extrato_total = deposito_operacao(saldo, deposito, extrato_total)
        
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

    elif opcoes == 'e':
        extrato(saldo, extrato=extrato_total)

    elif opcoes == 'q':
        print("Obrigado por utilizar nosso sistema!")
        break

    else:
        print("Opção inválida! Por gentileza, selecione uma das opções"
              "do menu.")
