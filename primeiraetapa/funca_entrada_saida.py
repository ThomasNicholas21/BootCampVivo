#Este arquivo é destinado para estudo junto ao bootcampVivo 
#Terá anotações e código

# Funcoes output e input, são funcoes built-ins
# Output - print, aceita 4 argumentos sep, end, file e flush

#Exemplo de output
def calculos(numero1, numero2):
    adicao = numero1 + numero2
    subtracao = numero1 - numero2
    divisao = numero1 / numero2
    multiplicacao = numero1 * numero2
    return print(f"Soma:{adicao}\n"
                f"Subtracao:{subtracao}\n"
                f"Divisao:{divisao}\n"
                f"Multiplicacao:{multiplicacao}")

# Exemplo de input
numero1 = float(input('Digite o primeiro numero: '))
numero2 = float(input('Digite o primeiro numero: '))

calculos(numero1, numero2)