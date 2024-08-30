# *Sobre este Sistema* 💻
Se trata da primeira versão de um sistema bancário no qual deve-se ter as seguintes funcionalidades:
- Depósito
- Saque
- Extrato

# Terceira Versão
## Melhorias da Segunda Versão
Iniciar modelagem do sistema bancário em POO. O armazenamento de dados será em objetos ao invés de dicionários.
## Classes e Relações do Sistema Bancário

- ### Historico
    - **Atributos:**
        - Nenhum especificado.
    - **Métodos:**
        - `+ adicionar_transacao(transacao: Transacao)`

- ### Transacao (interface)
    - **Métodos:**
        - `+ registrar(conta: Conta)`

- ### Deposito
    - **Atributos:**
        - `- valor: float`

- ### Saque
    - **Atributos:**
        - `- valor: float`

- ### Conta
    - **Atributos:**
        - `- saldo: float`
        - `- numero: int`
        - `- agencia: str`
        - `- cliente: Cliente`
        - `- historico: Historico`
    - **Métodos:**
        - `+ saldo() : float`
        - `+ nova_conta(cliente: Cliente, numero: int) : Conta`
        - `+ sacar(valor: float) : bool`
        - `+ depositar(valor: float) : bool`

- ### ContaCorrente (herda de Conta)
    - **Atributos:**
        - `- limite: float`
        - `- limite_saques: int`

- ### Cliente
    - **Atributos:**
        - `- endereco: str`
        - `- contas: list`
    - **Métodos:**
        - `+ realizar_transacao(conta: Conta, transacao: Transacao)`
        - `+ adicionar_conta(conta: Conta)`

- ### PessoaFisica (herda de Cliente)
    - **Atributos:**
        - `- cpf: str`
        - `- nome: str`
        - `- data_nascimento: date`

- ## Relações:
    - **Historico** possui uma relação de 1 para * com **Transacao**.
    - **Conta** possui uma relação de 1 para * com **Cliente**.
    - **Cliente** realiza uma relação de 1 para * com **Transacao**.
    - **ContaCorrente** herda de **Conta**.
    - **PessoaFisica** herda de **Cliente**.
