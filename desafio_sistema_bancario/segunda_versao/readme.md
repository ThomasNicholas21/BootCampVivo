# *Sobre este Sistema* 💻
Se trata da primeira versão de um sistema bancário no qual deve-se ter as seguintes funcionalidades:
- Depósito
- Saque
- Extrato

# Melhorias da Primeira Versão
- # Separar funções existente:
    - ## *Função Deposito*:
        - Recebe apenas positional
        - Argumentos: saldo, valor e extrato
        - Retorno: saldo e extrato
    - ## *Função Saqu*e
        - Recebe apenas Kworgs
        - Argumentos: saldo, valor extrato, limite_numero_saques
        - Retornos saldo e extrato
    - ## *Função Extrato*
        - Positional only e keyword only
        - Argumentos posicionais: saldo e argumentos
        - Argumentos nomeados: extrato
- # Cadastrar Usuário:
    - Armazena os usuários em uma lista
    - Não pode cadastrar 2 usuários com o mesmo CPF
    - Usuário é composto por: Nome, data de nascimento, CPF e endereço
        - Endereço: logradouro, numero, bairro, cidade/sigla estado
            - CPF deve registrar apenas números
- # Criar conta corrente:
    - Armazenar conta em uma lista.
    - Usuario pode ter mais de uma conta, mas uma conta pertence somer a um usuário
    - Conta: agência, número da conta e usuário.
        - Número da conta deve ser sequencial, iniciando com 1.
        - Número da agência é fico "0001"
