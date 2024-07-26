class Bicicleta: # Definindo Classe
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self): # Metodo
        print('Bi-bi')
    
    def parar(self): # Metodo
        print('Parando Bicicleta')
    
    def correr(self): # Metodo
        print('Acelera bicicleta')

    def __str__(self): # Retorna uma string que represente o objeto
        return f'Características: {self.cor}, {self.modelo}, {self.ano} e {self.valor}'

# Instanciando objeto
bike1 = Bicicleta('Azul', 'BMX', 2004, 1400)
bike1.buzinar()
bike1.parar()
bike1.correr()
print(bike1.cor, bike1.modelo, bike1.ano, bike1.valor)
print(bike1)
        