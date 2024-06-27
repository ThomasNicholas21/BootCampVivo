# Sào estruturas utilizadas para repetir um trecho de código
# um determinado número de vezes.

# Comando for:
# utilizado para percorrer um objeto iterável, sendo utilizado
# quando sabemos a quantidade de vezes que o código deve ser utilizado.
# Exemplo

nome = 'Thomas'
vogais = 'aeiou'

for letra in nome:
    if letra.lower() in vogais:
        print(letra)
else:
    print('Finalizado')

# Exemplo

for contador in range(0, 10, 1):
    print(contador)