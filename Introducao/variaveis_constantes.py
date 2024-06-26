#Este arquivo é destinado para estudo junto ao bootcampVivo 
#Terá anotações e código

# Variáveis são recebidas e não necessáriamente 
# permanecem com o mesmo valor
# Constante é imutável, comeca com mesmo valor e permanece com mesmo.
# Não existe no python, porém por concao é deixar em maaiúsculo


#Boas práticas: "snake case", nome sugestivos, constantes maaiúsculo


# Exemplos de variáveis
def print_dados(nome, idade, email):
    return print(f'Seu nome é {nome} e tem {idade} anos. Seu e-mail de contato é {email}.')

# Exemplos de variáveis 
nome = 'Thomas'
idade = 23
email = 'thomasnicholaas@gmail.com'

print_dados(nome, idade,email)

nome = 'Guilherme'
idade = 28
email = 'guilherme@gmail.com'

print_dados(nome, idade, email)



