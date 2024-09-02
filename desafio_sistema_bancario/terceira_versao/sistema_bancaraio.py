from abc import ABC, abstractmethod

class Cliente:
    def __init__(self, endereco, contas=[]):
        self.endereco = str(endereco)
        self.contas = contas

    def realizar_transacao(self, conta, transacao):
        pass

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco, contas=[]):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        super().__init__(endereco, contas)

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self.numero = numero
        self.agencia = '0001'
        self.cliente = cliente
        self.historico = Historico()

    def saldo():
        pass

    def nova_conta():
        pass

    def sacar():
        pass

    def depositar(self, saldo, historico):
        pass
    
class ContaCorrente(Conta):
    def __init__(self, limite, limite_saques, saldo, numero, agencia):
        self.limite = limite
        self.limite_saques = limite_saques
        super().__init__(saldo, numero, agencia)

# Classe Abstrata
class Transacao(ABC):
    @abstractmethod
    def valor(self):
        pass
    
    @property
    @abstractmethod
    def registrar(self):
        pass

class Deposito(Transacao):
    pass

class Saque(Transacao):
    pass

class Historico:
    def __init__(self, transacoes=[]):
        self._transacoes = transacoes

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                'Tipo': transacao.__class__.__name__,
                'Valor': transacao.valor,
                'Data': 'Validar Operação Date Time'
            }
        ) 

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