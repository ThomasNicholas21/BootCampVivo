#Este arquivo é destinado para estudo junto ao bootcampVivo 
#Terá anotações e código

# A conversao de dados é somente quando necessário converter um tipo de dados para o outro

def convertor_tipo(numero):
    if isinstance(numero,(int, float)):
        numero_str = str(numero)
        return print(str(numero_str), type(numero_str))
    return print(numero, type(numero))

numero1 = '1'
numero2 = 2
numero3 = '3'
numero4 = 4

convertor_tipo(numero1)
convertor_tipo(numero2)
convertor_tipo(numero3)
convertor_tipo(numero4)