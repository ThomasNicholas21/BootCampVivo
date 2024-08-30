from abc import ABC, abstractmethod

class Cliente:
    pass

class PessoaFisica(Cliente):
    pass

class Conta:
    pass

class ContaCorrente(Conta):
    pass

class Historico:
    pass 

# Classe Abstrata
class Transacao:
    pass

class Deposito(Transacao):
    pass

class Saque(Transacao):
    pass

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

    while True:
        opcoes = input(menu()).lower().strip() # Chama a função menu para o usuário selecionar qual a opção desejada
        if opcoes == 'd': # Caso o usuário deseje depositar
            pass
            
        elif opcoes == 's': # Caso o usuário deseje sacar
            pass

        elif opcoes == 'e': # Caso o usuário deseje visualizar o extrato
            pass
        
        elif opcoes == 'c': # Caso o usuário deseje cadastrar um usuário
            pass
        
        elif opcoes == 'ccc': # Caso o usuário deseje criar um contato corrente
            pass
        
        elif opcoes == 'lu': # Caso o usuário deseje listar os dados de um usuário especifico
            pass
        
        elif opcoes == 'lc': # Caso o usuário deseje listar contas especificas
            pass

        elif opcoes == 'q': # Caso o usuário deseje encerrar o programa
            print("Obrigado por utilizar nosso sistema!")
            break

        else: # Caso o usuário erre o menu
            print("Opção inválida! Por gentileza, selecione uma das opções"
                "do menu.")
            
main()