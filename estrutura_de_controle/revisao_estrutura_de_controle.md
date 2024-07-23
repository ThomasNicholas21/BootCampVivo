# Revisão de estrutura de controle 💻
## Operadores
- ### Operadores de identificação
    - **`is`**: Verifica se duas variáveis apontam para o mesmo objeto na memória.
    ```python
    a = [1, 2, 3]
    b = a
    c = a[:]
    print(a is b)  # True
    print(a is c)  # False
    ```
    - **`is not`**: Verifica se duas variáveis não apontam para o mesmo objeto na memória.
    ```python
    print(a is not c)  # True
    ```

- ### Operadores Aritiméticos
    - **`+`**: Soma.
    ```python
    print(2 + 3)  # 5
    ```
    - **`-`**: Subtração.
    ```python
    print(5 - 2)  # 3
    ```
    - **`*`**: Multiplicação.
    ```python
    print(3 * 4)  # 12
    ```
    - **`/`**: Divisão.
    ```python
    print(10 / 2)  # 5.0
    ```
    - **`//`**: Divisão inteira.
    ```python
    print(10 // 3)  # 3
    ```
    - **`%`**: Módulo (resto da divisão).
    ```python
    print(10 % 3)  # 1
    ```
    - **`**`**: Exponenciação.
    ```python
    print(2 ** 3)  # 8
    ```

- ### Operadores de Associação
    - **`in`**: Verifica se um valor está presente em uma sequência.
    ```python
    print('a' in 'banana')  # True
    ```
    - **`not in`**: Verifica se um valor não está presente em uma sequência.
    ```python
    print('x' not in 'banana')  # True
    ```

- ### Operadores de Atribuição
    - **`=`**: Atribuição de valor.
    ```python
    x = 5
    ```
    - **`+=`**: Adição e atribuição.
    ```python
    x += 3  # x agora é 8
    ```
    - **`-=`**: Subtração e atribuição.
    ```python
    x -= 2  # x agora é 6
    ```
    - **`*=`**: Multiplicação e atribuição.
    ```python
    x *= 4  # x agora é 24
    ```
    - **`/=`**: Divisão e atribuição.
    ```python
    x /= 3  # x agora é 8.0
    ```
    - **`//=`**: Divisão inteira e atribuição.
    ```python
    x //= 2  # x agora é 4.0
    ```
    - **`%=`**: Módulo e atribuição.
    ```python
    x %= 3  # x agora é 1.0
    ```
    - **`**=`**: Exponenciação e atribuição.
    ```python
    x **= 3  # x agora é 1.0
    ```

- ### Operadores de Comparação
    - **`==`**: Igualdade.
    ```python
    print(3 == 3)  # True
    ```
    - **`!=`**: Diferença.
    ```python
    print(3 != 2)  # True
    ```
    - **`>`**: Maior que.
    ```python
    print(5 > 3)  # True
    ```
    - **`>=`**: Maior ou igual.
    ```python
    print(3 >= 3)  # True
    ```
    - **`<`**: Menor que.
    ```python
    print(2 < 3)  # True
    ```
    - **`<=`**: Menor ou igual.
    ```python
    print(3 <= 3)  # True
    ```
- ### Operadores Lógicos
    - **`and`**: Retorna `True` se ambas as expressões forem verdadeiras.
    ```python
    print(True and False)  # False
    ```
    - **`or`**: Retorna `True` se pelo menos uma das expressões for verdadeira.
    ```python
    print(True or False)  # True
    ```
    - **`not`**: Inverte o valor lógico.
    ```python
    print(not True)  # False
    ```

## Estrutura Condicional
- **`if`**: Executa um bloco de código se a condição for verdadeira.
    ```python
    x = 10
    if x > 5:
        print("x é maior que 5")  # Saída: x é maior que 5
    ```
- **`if-else`**: Executa um bloco de código se a condição for verdadeira, senão executa outro bloco de código.
    ```python
    x = 3
    if x > 5:
        print("x é maior que 5")
    else:
        print("x é menor ou igual a 5")  # Saída: x é menor ou igual a 5
    ```
- **`elif`**: Verifica múltiplas condições. Se a condição `if` for falsa, verifica a condição `elif`.
    ```python
    x = 5
    if x > 5:
        print("x é maior que 5")
    elif x == 5:
        print("x é igual a 5")  # Saída: x é igual a 5
    else:
        print("x é menor que 5")
    ```

- **`if`** aninhado
    - São condicionais dentro de condicionais, permitindo verificar múltiplas condições em níveis diferentes.
        ```python
        x = 10
        if x > 5:
            print("x é maior que 5")
            if x > 8:
                print("x é também maior que 8")  # Saída: x é maior que 5
                                                #         x é também maior que 8
        ```

- **`if`** ternário
    - Condição em uma única linha. Avalia a condição e retorna um valor com base no resultado.
        ```python
        x = 10
        resultado = "Maior que 5" if x > 5 else "Menor ou igual a 5"
        #"retorno da primeira condição" if condição else "retorno da segunda"
        print(resultado)  # Saída: Maior que 5
        ```
## Estrutura de Repetição

## Indentação

## Manipulação de String
- ### Fatiamento de String

- ### Interpolação de Variáveis

- ### Metodos para String

