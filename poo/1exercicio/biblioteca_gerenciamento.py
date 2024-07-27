# Atividade: Sistema de Gerenciamento de Biblioteca
# Objetivo: Criar um sistema simples para gerenciar uma biblioteca, utilizando classes, objetos, métodos construtores e destrutores.
# Descrição: Você irá criar três classes principais: Livro, Usuario, e Biblioteca.
# 1. Classe Livro
# Atributos: titulo (string) autor (string) ano_publicacao (int) disponivel (boolean, inicializado como True)
class Livro: # Construtor que inicializa todos os atributos do livro.
    def __init__(self, titulo, autor, ano_publicacao, disponivel=True):
        self.titulo = str(titulo)
        self.autor = str(autor)
        self.ano_publicacao = int(ano_publicacao)
        self.disponivel = bool(disponivel)

# Métodos:
# Método para marcar o livro como emprestado (disponivel se torna False).
def emprestar_livro(self):
    self.disponivel = False
    return self.disponivel

# Método para marcar o livro como devolvido (disponivel se torna True).
def devolver_livro(self):
    self.disponivel = True
    return self.disponivel

# Método destrutor que imprime uma mensagem quando um objeto Livro é destruído.
def __del__(self):
    print('Excluindo Livro.')

# 2. Classe Usuario
# Atributos: nome (string) livros_emprestados (lista de objetos Livro, inicializada como uma lista vazia)
# Métodos:
# Construtor que inicializa o nome do usuário.
# Método para emprestar um livro (adiciona o livro à lista livros_emprestados e marca o livro como emprestado).
# Método para devolver um livro (remove o livro da lista livros_emprestados e marca o livro como disponível).
# Método destrutor que imprime uma mensagem quando um objeto Usuario é destruído.
# 3. Classe Biblioteca
# Atributos: livros (lista de objetos Livro, inicializada como uma lista vazia) usuarios (lista de objetos Usuario, inicializada como uma lista vazia)
# Métodos:
# Construtor que inicializa as listas de livros e usuários.
# Método para adicionar um livro à biblioteca.
# Método para adicionar um usuário à biblioteca.
# Método para listar todos os livros disponíveis.
# Método para listar todos os usuários cadastrados.
# Método destrutor que imprime uma mensagem quando um objeto Biblioteca é destruído.
# Tarefas:
# Implemente as três classes descritas acima.
# Crie alguns objetos Livro e Usuario para testar seu sistema.
# Adicione os livros e usuários à Biblioteca.
# Faça alguns testes de empréstimo e devolução de livros.
# Liste os livros disponíveis e os usuários cadastrados para verificar se tudo está funcionando corretamente.