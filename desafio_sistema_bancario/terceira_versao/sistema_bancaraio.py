from abc import ABC, abstractmethod

class Cliente:
    def __init__(self, endereco, contas=[]):
        self.endereco = str(endereco)
        self.contas = contas

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

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
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self.cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo_excedido = valor > self._saldo
        if saldo_excedido:
            print('Saldo excedido, operação falhou!')
        
        elif  0 < valor < 500:
            self._saldo -= valor
            print('Operação concluida, saque efetuado!')
            return True
        
        elif valor > 500:
            print('Valor máximo atingido, tente uma valor abaixo de 500.')

        else:
            print('Operação desconhecida, valor inválido.')

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print('Deposito realizado, operação concluida!')
            return True
        else:
            print('Operação desconhecida, valor inválido. ')
    
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saque = len([transacao for transacao in self.historico.transacoes if transacao['Tipo'] == Saque.__name__])
        
        if numero_saque > self._limite_saques:
            print('Limite de sque diário atingido.')
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f'Agência:{self.agencia}\nNúmero:{self.numero}\nTitular:{self.cliente.nome}'

# Classe Abstrata
class Transacao(ABC):
    @abstractmethod
    def valor(self):
        pass
    
    @property
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        transacao_efetuada = conta.depositar(self.valor)

        if transacao_efetuada:
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        transacao_efetuada = conta.sacar(self.valor)

        if transacao_efetuada:
            conta.historico.adicionar_transacao(self)

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

def filtro_cliente(cpf, clientes):
    filtro = [cliente for cliente in clientes if cliente.cpf == cpf]
    return filtro[0] if filtro else None

def filtro_conta(cliente):
    if not cliente.contas:
        print('Cliente sem conta!')
    return cliente.contas[0]

def depositar(clientes):
    cpf = input('Informe o CPF:')
    cliente = filtro_cliente(cpf, clientes)

    if not cliente:
        print('Cliente não encontrado!')
        return 
    
    valor = float(input("Insira a quantidade que será depositada: ")) 
    transacao = Deposito(valor)

    conta = filtro_conta(cliente)
    
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input('Informe seu CPF:')
    cliente = filtro_cliente(cpf, clientes)

    if not cliente:
        print('Cliente não encontrado!')
        return
    
    valor = float(input("Informe quanto deseja sacar: "))
    transacao = Saque(valor)

    conta = filtro_conta(cliente)

    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

teste1 = PessoaFisica('cpf', 'nome', 'data_nascimento', 'endereco')
conta_teste1 = ContaCorrente(numero='1', cliente=teste1)
teste1.adicionar_conta(conta_teste1)
def main():
    clientes = [teste1]
    contas = [conta_teste1]

    while True:
        opcoes = input(menu()).lower().strip() # Chama a função menu para o usuário selecionar qual a opção desejada
        if opcoes == 'd': # Caso o usuário deseje depositar
            depositar(clientes)
            
        elif opcoes == 's': # Caso o usuário deseje sacar
            sacar(clientes)

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