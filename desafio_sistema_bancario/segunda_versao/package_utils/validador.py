import re

def verifica_letras_operadores(cpf): # Função de validação de operadores e letra
    validacao = r"[a-zA-Z+\-*/]"
    return bool(re.search(validacao, cpf)) # Retorna True se letras e operadores estiverem presentes
    
def verifica_cpf_cadastrado(cpf, lista_de_dados): # Valida se o CPF está cadastrado
    for dados in lista_de_dados:
        if dados['CPF'] == cpf:
            return True
    return False