# Atividade: Sistema de Gerenciamento de Biblioteca
# Objetivo: Criar um sistema simples para gerenciar uma biblioteca, utilizando classes, objetos, métodos construtores e destrutores.
# Descrição: Você irá criar três classes principais: Livro, Usuario, e Biblioteca.

class Livro: # Construtor que inicializa todos os atributos do livro.
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = str(titulo)
        self.autor = str(autor)
        self.ano_publicacao = int(ano_publicacao)
        self.disponivel = True

    def livro_emprestado(self):
        if self.disponivel:
            self.disponivel = False
        else:
            print(f'Livro {self.titulo} Disponivel.')

    def livro_disponivel(self):
        if self.disponivel == True:
            return f'Livro {self.titulo} disponível.'
        return f'Livro {self.titulo} indiponível.'
    
    def __str__(self):
        return f'Livro: {self.titulo}, Autor: {self.autor}, Publicacao: {self.ano_publicacao}, Disponível: {self.disponivel}'

    def __del__(self): # O mesmo não é necessário, pois o python possui um coletor de lixo
        pass

class Usuario: # Construtor que inicializa o nome do usuário.
    def __init__(self, nome):
        self.nome = str(nome)
        self.livros_emprestados = []

    def emprestar_livro(self, livros):
        if livros.disponivel:
            livros.livro_emprestado()

    def receber_livro(self, livros_emprestados):
        emprestimo = self.livro_disponivel()
        livros_emprestados.remove(emprestimo)

    def __del__(self):
        print(f'{self.nome}: Usuário destruidos.')
    
class Biblioteca: 
    def __init__(self, livros=[], usuarios=[]):
        self.livros = livros
        self.usuarios = usuarios

# Método para adicionar um livro à biblioteca.
    def adiciona_livro(self, livros):
        livros.append(Livro)
# Método para adicionar um usuário à biblioteca.
    def adicionar_usuario(self, usuarios):
        ...
# Método para listar todos os livros disponíveis.
    def lista_livros(self, livros):
        ...
# Método para listar todos os usuários cadastrados.
    def lista_usuarios(self, usuarios):
        ...
# Método destrutor que imprime uma mensagem quando um objeto Biblioteca é destruído.
    def __del__(self):
        print('Objeto destruido.')

# Tarefas:
# Implemente as três classes descritas acima.
# Crie alguns objetos Livro e Usuario para testar seu sistema.
# Adicione os livros e usuários à Biblioteca.
# Faça alguns testes de empréstimo e devolução de livros.
# Liste os livros disponíveis e os usuários cadastrados para verificar se tudo está funcionando corretamente.


livro1 = Livro('Cosmos', 'Carl Segan', 1980, True)
livro2 = Livro('Rápido e Devagar', 'Daniel Kahneman', 2011, False)
print(livro1.livro_disponivel())
print(livro2.livro_disponivel())
print(livro1.livro_emprestado())
print(livro2.livro_emprestado())