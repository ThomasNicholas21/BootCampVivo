# Revisão de estrutura de controle 💻
## Indentação
- **`Indentação`**: O objetivo é manter o código fonte limpo, legível e manutenível. Em Python, a indentação é obrigatória e indica blocos de código.
    ```python
    if x > 0:
        print("x é positivo")
    ```
- **`Interpretador`**: Python consegue determinar onde o bloco inicia e onde ele termina através da indentação. Cada nível de indentação geralmente consiste em 4 espaços.
    ```python
    for i in range(5):
        if i % 2 == 0:
            print(f"{i} é par")
    ```

## Clean Code Python
- ### Importância de Clean Code
Manter o código limpo e legível é essencial para facilitar a manutenção, aumentar a produtividade e reduzir erros. Aqui estão algumas dicas importantes para escrever clean code em Python:

- ### Dicas de Clean Code
    - **Use Nomes Descritivos**: Variáveis, funções e classes devem ter nomes claros e descritivos.
        ```python
        # Bom
        def calcular_media(lista_de_numeros):
            # ...
        
        # Ruim
        def calc(lst):
            # ...
        ```

    - **Evite Comentários Desnecessários**: Comente apenas o necessário. O código deve ser autoexplicativo sempre que possível.
        ```python
        # Bom
        def verificar_se_eh_par(numero):
            return numero % 2 == 0
        
        # Ruim
        def verificar_se_eh_par(numero):
            # Verifica se o número é par
            return numero % 2 == 0
        ```

    - **Mantenha Funções e Métodos Curtos**: Funções e métodos devem fazer apenas uma coisa e fazê-la bem. Idealmente, não devem ter mais de 20 linhas.
        ```python
        # Bom
        def obter_dados_usuario():
            # ...
        
        def validar_dados_usuario():
            # ...
        
        # Ruim
        def obter_e_validar_dados_usuario():
            # ...
        ```

    - **Use Espaços em Branco para Melhorar a Legibilidade**: Utilize linhas em branco para separar blocos de código e melhorar a leitura.
        ```python
        # Bom
        def funcao_exemplo():
            valor = calcular_valor()
            
            if valor > 0:
                processar_valor(valor)
            
            return valor
        
        # Ruim
        def funcao_exemplo():
            valor = calcular_valor()
            if valor > 0:
                processar_valor(valor)
            return valor
        ```

    - **Consistência na Indentação**: Use 4 espaços por nível de indentação. Não misture espaços e tabulações.
        ```python
        # Bom
        for i in range(10):
            print(i)
            
        # Ruim
        for i in range(10):
        print(i)
        ```

    - **Evite Códigos Duplicados**: Se você se pegar copiando e colando código, considere refatorar para uma função ou método.
        ```python
        # Bom
        def calcular_area_retangulo(largura, altura):
            return largura * altura
        
        area1 = calcular_area_retangulo(10, 20)
        area2 = calcular_area_retangulo(15, 30)
        
        # Ruim
        area1 = 10 * 20
        area2 = 15 * 30
        ```

    - **Seja Explícito**: Prefira ser explícito ao invés de implícito. Código explícito é mais fácil de entender e menos propenso a erros.
        ```python
        # Bom
        def verificar_maioridade(idade):
            if idade >= 18:
                return True
            else:
                return False
        
        # Ruim
        def verificar_maioridade(idade):
            return idade >= 18
        ```

    - **Trate Exceções de Forma Apropriada**: Sempre lide com exceções, mas faça isso de forma que o código continue sendo legível e compreensível.
        ```python
        # Bom
        try:
            resultado = operacao_critica()
        except ErroEsperado as e:
            tratar_erro(e)
        
        # Ruim
        try:
            resultado = operacao_critica()
        except:
            pass
        ```

    - **Utilize List Comprehensions**: São uma maneira concisa e eficiente de criar listas.
        ```python
        # Bom
        quadrados = [x**2 for x in range(10)]
        
        # Ruim
        quadrados = []
        for x in range(10):
            quadrados.append(x**2)
        ```

    - **Documente seu Código**: Use docstrings para documentar funções, classes e módulos.
        ```python
        def funcao_exemplo(parametro):
            """
            Esta função faz algo muito importante.
            
            Args:
                parametro (tipo): Descrição do parâmetro.
            
            Returns:
                tipo: Descrição do retorno.
            """
            # ...
        ```

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
    - **`Obersavação`**: Mais exemplos de interpolação de Variáveis ["clique aqui""](https://github.com/ThomasNicholas21/BootCampVivo/blob/master/estrutura_de_controle/operadores/oepradores_identidadae.py)

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
    - **`Obersavação`**: Mais exemplos de interpolação de Variáveis ["clique aqui""](https://github.com/ThomasNicholas21/BootCampVivo/blob/master/estrutura_de_controle/operadores/oepradores_identidadae.py)
- ### Operadores de Associação
    - **`in`**: Verifica se um valor está presente em uma sequência.
    ```python
    print('a' in 'banana')  # True
    ```
    - **`not in`**: Verifica se um valor não está presente em uma sequência.
    ```python
    print('x' not in 'banana')  # True
    ```
    - **`Obersavação`**: Mais exemplos de interpolação de Variáveis ["clique aqui""](https://github.com/ThomasNicholas21/BootCampVivo/blob/master/estrutura_de_controle/operadores/operadores_associcao.py)
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
    - **`Obersavação`**: Mais exemplos de interpolação de Variáveis ["clique aqui""](https://github.com/ThomasNicholas21/BootCampVivo/blob/master/estrutura_de_controle/operadores/operadores_atribuicao.py)
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
    - **`Obersavação`**: Mais exemplos de interpolação de Variáveis ["clique aqui""](https://github.com/ThomasNicholas21/BootCampVivo/blob/master/estrutura_de_controle/operadores/operadores_comparacao.py)
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
    - **`Obersavação`**: Mais exemplos de interpolação de Variáveis ["clique aqui""](https://github.com/ThomasNicholas21/BootCampVivo/blob/master/estrutura_de_controle/operadores/operadores_logicos.py)
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

- **`Obersavação`**: Mais exemplos de interpolação de Variáveis ["clique aqui""](https://github.com/ThomasNicholas21/BootCampVivo/blob/master/estrutura_de_controle/condicional_repeticao/estrutura_condicionais.py)
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

- **`Obersavação`**: Mais exemplos de interpolação de Variáveis ["clique aqui""](https://github.com/ThomasNicholas21/BootCampVivo/blob/master/estrutura_de_controle/condicional_repeticao/estrutura_repeticao.py)

## Manipulação de String
- ## Fatiamento de String
    - **`string[start:stop:step]`**: Permite extrair partes de uma string.
        - **`start`**: Posição inicial (inclusiva, padrão é 0).
        - **`stop`**: Posição final (exclusiva, padrão é o final da string).
        - **`step`**: Passo entre os índices (padrão é 1).
        ```python
        texto = "Hello, World!"
        print(texto[0:5])    # Saída: Hello
        print(texto[7:12])   # Saída: World
        print(texto[::2])    # Saída: Hlo ol!
        print(texto[::-1])   # Saída: !dlroW ,olleH
        ```
    - **`Obersavação`**: Mais exemplos de interpolação de Variáveis ["clique aqui""](https://github.com/ThomasNicholas21/BootCampVivo/blob/master/estrutura_de_controle/manipulacao_string/fatiamento_strings.py)
- ## Interpolação de Variáveis
    - `%` - Versão Antiga
        - Utiliza o operador `%` para inserir variáveis dentro de strings.
            ```python
            nome = "Alice"
            idade = 30
            print("Nome: %s, Idade: %d" % (nome, idade))
            # Saída: Nome: Alice, Idade: 30
            ```

    - `format` - Especifica de Forma Automática
        - Usa o método `str.format()` para substituir os placeholders `{}` pela ordem dos argumentos fornecidos.
            ```python
            nome = "Bob"
            idade = 25
            print("Nome: {}, Idade: {}".format(nome, idade))
            # Saída: Nome: Bob, Idade: 25
            ```

    - `format` - Especifica de Forma Manual
        - Usa índices numéricos para especificar a ordem dos argumentos nos placeholders `{}`.
            ```python
            nome = "Carol"
            idade = 28
            print("Nome: {0}, Idade: {1}".format(nome, idade))
            # Saída: Nome: Carol, Idade: 28
            print("Idade: {1}, Nome: {0}".format(nome, idade))
            # Saída: Idade: 28, Nome: Carol
            ```

    - `format` - Especifica de Forma Lógica
        - Usa nomes de variáveis nos placeholders `{}` que correspondem aos argumentos nomeados fornecidos.
            ```python
            print("Nome: {nome}, Idade: {idade}".format(nome="Dave", idade=35))
            # Saída: Nome: Dave, Idade: 35
            ```

    - `format` - Desempacotando Dicionário
        - Usa a sintaxe `**` para desempacotar um dicionário e substituir os placeholders `{}` pelos valores correspondentes.
            ```python
            pessoa = {"nome": "Eve", "idade": 22}
            print("Nome: {nome}, Idade: {idade}".format(**pessoa))
            # Saída: Nome: Eve, Idade: 22
            ```

    - `f-strings`
        - Utiliza a sintaxe `f"{variável}"` para inserir variáveis diretamente dentro de strings. Disponível a partir do Python 3.6.
            ```python
            nome = "Frank"
            idade = 40
            print(f"Nome: {nome}, Idade: {idade}")
            # Saída: Nome: Frank, Idade: 40
            ```
    - **`Obersavação`**: Mais exemplos de interpolação de Variáveis ["clique aqui""](https://github.com/ThomasNicholas21/BootCampVivo/blob/master/estrutura_de_controle/manipulacao_string/interpolacao_variaveis.py)

- ## Métodos para String
    - **`string.upper()`**: Converte todos os caracteres para maiúsculo.
        ```python
        texto = "python"
        print(texto.upper())
        # Saída: PYTHON
        ```

    - **`string.lower()`**: Converte todos os caracteres para minúsculo.
        ```python
        texto = "PYTHON"
        print(texto.lower())
        # Saída: python
        ```

    - **`string.title()`**: Converte o primeiro caractere de cada palavra para maiúsculo e o restante para minúsculo.
        ```python
        texto = "programação em python"
        print(texto.title())
        # Saída: Programação Em Python
        ```

    - **`string.strip()`**: Remove espaços em branco no início e no fim da string.
        ```python
        texto = "  python  "
        print(texto.strip())
        # Saída: python
        ```

    - **`string.lstrip()`**: Remove espaços em branco à esquerda da string.
        ```python
        texto = "  python"
        print(texto.lstrip())
        # Saída: python
        ```

    - **`string.rstrip()`**: Remove espaços em branco à direita da string.
        ```python
        texto = "python  "
        print(texto.rstrip())
        # Saída: python
        ```

    - **`string.center()`**: Alinha a string no centro, preenchendo com o caractere especificado até atingir o comprimento total desejado.
        ```python
        texto = "python"
        print(texto.center(10))
        # Saída: '  python  '
        print(texto.center(10, '-'))
        # Saída: --python--
        ```

    - **`string.split(sep, maxsplit)`**: Divide a string em uma lista com base no separador especificado. O `maxsplit` é opcional e define o número máximo de divisões.
        ```python
        texto = "python é divertido"
        print(texto.split())
        # Saída: ['python', 'é', 'divertido']
        print(texto.split(' ', 1))
        # Saída: ['python', 'é divertido']
        ```

    - **`'item'.join(string)`**: Junta os caracteres da string com o item especificado.
        ```python
        texto = "python"
        print('-'.join(texto))
        # Saída: p-y-t-h-o-n
        ```

    - **`string.replace(old, new, count)`**: Substitui todas as ocorrências da substring `old` por `new`. O argumento `count` é opcional e limita o número de substituições.
        ```python
        texto = "python é divertido"
        print(texto.replace("python", "programação"))
        # Saída: programação é divertido
        ```

    - **`string.startswith(prefix)`**: Verifica se a string começa com o prefixo especificado.
        ```python
        texto = "python é divertido"
        print(texto.startswith("python"))
        # Saída: True
        ```

    - **`string.endswith(suffix)`**: Verifica se a string termina com o sufixo especificado.
        ```python
        texto = "python é divertido"
        print(texto.endswith("divertido"))
        # Saída: True
        ```

    - **`string.find(sub)`**: Retorna o índice da primeira ocorrência da substring `sub`. Retorna -1 se a substring não for encontrada.
        ```python
        texto = "python é divertido"
        print(texto.find("divertido"))
        # Saída: 12
        ```

    - **`string.count(sub)`**: Conta quantas vezes a substring `sub` aparece na string.
        ```python
        texto = "python é divertido, python é fácil"
        print(texto.count("python"))
        # Saída: 2
        ```

    - **`string.zfill(width)`**: Preenche a string com zeros à esquerda até atingir o comprimento especificado.
        ```python
        texto = "42"
        print(texto.zfill(5))
        # Saída: 00042
        ```

    - **`string.isdigit()`**: Verifica se todos os caracteres na string são dígitos.
        ```python
        texto = "12345"
        print(texto.isdigit())
        # Saída: True
        ```

    - **`string.isalpha()`**: Verifica se todos os caracteres na string são letras.
        ```python
        texto = "python"
        print(texto.isalpha())
        # Saída: True
        ```
    - **`Obersavação`**: Mais exemplos de interpolação de Variáveis ["clique aqui""](https://github.com/ThomasNicholas21/BootCampVivo/blob/master/estrutura_de_controle/manipulacao_string/metodo_string.py)
