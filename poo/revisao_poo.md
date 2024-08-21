# Pragramação Orientada a Objetos (POO)
Paradigma de programação é um estilo de programação de como solucionar problemas através do código. O paradigma de programação orientada a objetos faz a estruturação do código abstraindo problemas em objetos do mundo real, facilitando o entendimento do código e tornando-o mais flexível e modular.

## Classes e Objetos
- **```Classes```**
    - É o que define as características e comportamentos de um objeto, porém não é possível utilizar diretamente, ou seja, é algo abstrato.
- **```Objetos```**
    - O objeto instanciado por uma classe pode utilizar as características e comportamentos que foram definidos na classe.

Exemplo:
```python
class Calculadora:
    def somar(self, a, b):
        return a + b

calc = Calculadora()
resultado = calc.somar(3, 4)
print(resultado)  # 7
```
- [Mais exemplos](https://github.com/ThomasNicholas21/BootCampVivo/tree/master/poo/classes_objetos)

## Contrutores e Destrutores
- **```Método Contrutor```**
    - Inicializa de forma automática os atributos do objeto, chamado quando uma nova instância da classe é criada, sendo chamado de: ```__init__ ```
    Exemplo:
    ```python
    class MinhaClasse:
        def __init__(self, parametros):
            # Inicialização dos atributos
            self.atributo1 = valor1
            self.atributo2 = valor2
    ```
- **```Método Destrutor```**
    - Ele é chamado para realizar a destruição de um objeto, ou seja, para remover o objeto da memória. Ele é menos utilizado em Python, pois a linguagem possui um recurso de coletor de lixo, porém aquele que não é removido o método se torna útil, como por exemplo: conexões de rede ou recursos externos. Sendo representado por: ```__del__```.

    Exemplo:
    ```python
    class Pessoa:
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade
            print(f'{self.nome} foi criado.')

        def __del__(self):
            print(f'{self.nome} está sendo destruído.')git s

    # Criando uma instância da classe Pessoa
    pessoa1 = Pessoa("João", 30)

    # Deletando a instância explicitamente
    del pessoa1
    ```
- [Mais exemplos](https://github.com/ThomasNicholas21/BootCampVivo/tree/master/poo/construtores_destrutores)

## Herança
- **O que é?**
    - Na programação orientada a objeto, herança é a capacidade de uma classe filha herdar as caractéristicas e comportamento da classe pai.
- **Vatangens:**
    - Faz a reutilização do código, para que não seja necessário repetir. Além disso, permite adicionar mais recursos a uma classe sem modificá-la.
    - É transitiva, caso uma classe B herde da classe A, todas as sublcasses de B heradarão de forma automatica da classe A, ou seja, caso a classe B tenha como filha a classe C, essa classe será neta da classe A herdando suas caractéristicas.
        - **Obs:** Sempre verificar a complexidade da herança das classe, pois caso a fámilia seja grande, uma pequena alteração irá refletir em toda a familia.
## **Herança Simples**
- Quando uma classe filha herda apenas uma classe pai, essa é chamada de herança simples 
```python
class A:
    pass
class B(A): # Filha da classe A
    pass
```
## **Herança Múltipla**
- Quando uma classe filha herda de várias classes pai, ela é chamada de herança múltipla.
```python
class A:
    pass
class B: 
    pass
class C(A, B): # Herda caractéristicas da classe A e B
    pass
```

## Encapsulamento
- **O que é?**
    - É a ideia de agrupar dados, impondo métodos que manipulam os dados. Impondo restrições diretos a variáveis e métodos, evitando a modificação de dados, pódendo apenas ser modificada pelo método do dado. Garantindo a manipulação de dados de forma consistente e segura.
- **Como funciona?**
    - **Atributos públicos:** Acessíveis de qualquer lugar.
    - **Atributos protegidos:** Acessíveis dentro de classes e subclasses (Indicado por "_")
        - **Um "_":** Isso indica uma convenção, sinalizando que o metodo indicado é protegido e deve ser tratado como detalhe interno.
        ### **Exemplo:**
        ```python
        class conta_bancaria:
            def __init__(self, titular, saldo_inicial):
                self.titular = titular # Atributo público
                self._saldo = saldo_inicial # Atributo Protegido
        ```
    - **Atributos privados:** Acessíveis apenas dentro da classe (Indicado por "__")
        - **Dois "__":** Este indica que o atributo passará por um processo chamado **Name Mangling** tornando o mesmo privado, pois ele dificulta o acesso fora da classe. O mesmo deixa o atributo diferente do que ele foi declarado de forma intencional. **Exemplo**
        ``` Python
        class conta_bancaria:
            def __init__(self, titular, saldo_inicial):
                self.titular = titular # Atributo público
                self.__saldo = saldo_inicial # Atributo Privado
            
            def obter_saldo(self):
                return self.__saldo 
        ```


