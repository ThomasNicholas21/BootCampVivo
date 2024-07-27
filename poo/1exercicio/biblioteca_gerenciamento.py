# Atividade: Sistema de Gerenciamento de Biblioteca
# Objetivo: Criar um sistema simples para gerenciar uma biblioteca, utilizando classes, objetos, métodos construtores e destrutores.
# Descrição: Você irá criar três classes principais: Livro, Usuario, e Biblioteca.

# Atributos: titulo (string) autor (string) ano_publicacao (int) disponivel (boolean, inicializado como True)
class Livro: # Construtor que inicializa todos os atributos do livro.
    def __init__(self, titulo, autor, ano_publicacao, disponivel=True):
        self.titulo = str(titulo)
        self.autor = str(autor)
        self.ano_publicacao = int(ano_publicacao)
        self.disponivel = bool(disponivel)

# Método para marcar o livro como emprestado (disponivel se torna False).
    def livro_emprestado(self):
        self.disponivel = False
        return self.disponivel

# Método para marcar o livro como devolvido (disponivel se torna True).
    def livro_disponivel(self):
        self.disponivel = True
        return self.disponivel

# Método destrutor que imprime uma mensagem quando um objeto Livro é destruído.
    def __del__(self):
        print(f'{self.titulo} está sendo excluido.')

# Atributos: nome (string) livros_emprestados (lista de objetos Livro, inicializada como uma lista vazia)
class Usuario(Livro): # Construtor que inicializa o nome do usuário.
    def __init__(self, nome, livros_emprestados=[]):
        self.nome = str(nome)
        self.livros_emprestados = list(livros_emprestados)

# Método para emprestar um livro (adiciona o livro à lista livros_emprestados e marca o livro como emprestado).
    def emprestar_livro(self, livros_emprestados):
        emprestimo = self.livro_emprestado()
        livros_emprestados.append(emprestimo)

# Método para devolver um livro (remove o livro da lista livros_emprestados e marca o livro como disponível).
    def receber_livro(self, livros_emprestados):
        emprestimo = self.livro_disponivel()
        livros_emprestados.remove(emprestimo)

# Método destrutor que imprime uma mensagem quando um objeto Usuario é destruído.
    def __del__(self):
        print(f'{self.nome}: Usuário destruidos.')
    
# Atributos: livros (lista de objetos Livro, inicializada como uma lista vazia) usuarios (lista de objetos Usuario, inicializada como uma lista vazia)
class Biblioteca: # Construtor que inicializa as listas de livros e usuários.
    def __init__(self, livros=[], usuarios=[]):
        self.livros = livros
        self.usuarios = usuarios

# Método para adicionar um livro à biblioteca.
    def adiciona_livro(self, livros):
        ...
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