# Operadores cuja a finalidade será de montar uma expressão lógica
# retornando um boleano
# Operador "e"
# and - ambos precisam ser verdade para retornar verdade
# Operador "ou"
# or - apenas um precisa retornar verdade
# Operador "não"
# not - inverso da verdade
# Parênteses da prioridade para operação

#Exemplos

def valida_saque_disponivel(saque):
    if saque > 0 and <=200:
        return print('Saque disponivel')
    return print('Seu saque limite é menor que 200')

def valida_limite_disponivel(limite):
    limite_disponivel = 1000
    if not limite == limite_disponivel:
        return print('Indisponivel')
    return print('Disponivel')

def libera_saque():
    nome = input('Insira seu nome:')
    cpf = input('Insira seu CPF:')
    senha = input('Insira sua senha: ')
    verifica_usuario_simples(nome, cpf, senha)
    if verifica_usuario_simples is True:
        return print('Saque liberado.')
    return print('Saque negado.')

def verifica_usuario_simples(name, cpf, senha, lista):
    if (name and cpf and senha) in lista:
        return True
    return False

lista = ['Thomas', '01862859202', '123']
valida_limite_disponivel(150)