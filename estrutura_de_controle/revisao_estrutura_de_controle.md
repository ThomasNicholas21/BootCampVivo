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
- ### `for` e `for-else`
    - **`for`**: Utilizado para iterar sobre uma sequência (como uma lista, tupla ou string).
        ```python
        for i in range(5):
            print(i)
        # Saída: 0, 1, 2, 3, 4
        ```
    - **`for-else`**: O bloco `else` é executado quando o loop é concluído normalmente, ou seja, não foi interrompido por um `break`, caso seja, o `else` não é executado.
        ```python
        for i in range(5):
            print(i)
        else:
            print("Loop concluído sem interrupção.")
        # Saída: 0, 1, 2, 3, 4
        #         Loop concluído sem interrupção.

        ```

- ### `while`
    - Utilizado para repetir um bloco de código enquanto a condição for verdadeira.
        ```python
        x = 0
        while x < 5:
            print(x)
            x += 1
        # Saída: 0, 1, 2, 3, 4
        ```
    - **`while-else`**:
    ```python
        x = 0
        while x < 5:
            print(x)
            x += 1
        else:
            print('Contagem concluída sem interreupção!')
        # Saída: 0, 1, 2, 3, 4
        #         Contagem concluída sem interreupção!
    ```
- ### `break`
    - Utilizado para interromper o loop imediatamente.
        ```python
        for i in range(5):
            if i == 3:
                break
            print(i)
        # Saída: 0, 1, 2
        ```

- ### `continue`
    - Utilizado para pular a iteração atual e continuar com a próxima.
        ```python
        for i in range(5):
            if i == 3:
                continue
            print(i)
        # Saída: 0, 1, 2, 4
        ```

- ### `pass`
    - Utilizado como um placeholder em um loop, função ou classe, indicando que nada deve ser feito.
        ```python
        for i in range(5):
            if i == 3:
                pass
            print(i)
        # Saída: 0, 1, 2, 3, 4
        ```

- ### Momentos Ideais para Uso
    - **`for`**: Ideal para iterar sobre elementos de uma sequência, quando você sabe antecipadamente quantas iterações são necessárias.
    - **`for-else`**: Útil quando você precisa executar um código após a conclusão do loop, mas apenas se o loop não foi interrompido.
    - **`while`**: Ideal quando você não sabe antecipadamente quantas iterações serão necessárias e a repetição depende de uma condição.
    - **`break`**: Útil para sair de um loop antes que todas as iterações sejam concluídas, geralmente usado dentro de uma condição.
    - **`continue`**: Útil para pular a iteração atual e continuar com a próxima, geralmente usado para ignorar certos casos dentro de um loop.
    - **`pass`**: Útil como um placeholder quando a sintaxe exige um comando, mas você não quer executar nenhuma ação no momento.

## Indentação

## Manipulação de String
- ### Fatiamento de String

- ### Interpolação de Variáveis

- ### Metodos para String

