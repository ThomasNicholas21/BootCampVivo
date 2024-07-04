# Métodos úteis para manipulação de string
# string.upper() - todos caracteres para maiúsculo
# string.lower() - todos caracteres para minúsculo
# string.title() - Primeiro caractere Maiúsculo e o restante minúsculo
# string.strip() - remove espaços
# string.lstrip() - remove o espaço a esquerda
# string.rstrip() - remove o esparaço a direita
# string.center() - 2 argumentos sendo o segundo opcional; número de caracter, e com o que vai ser preenchido
# 'item'.join(string) -  junta o item na string

string = ' ThOmAs '
print(string.title())
print(string.lower())
print(string.upper())
print(string.strip())
print(string.lstrip())
print(string.rstrip())
print(string.center(10, '!'))
print('!'.join(string))