
"""
Desafio 5: A Estante de Livros
Muitas vezes, uma classe é composta por outras (Composição),
simulando o agrupamento de objetos reais.
 """

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f'{self.titulo} {self.autor}'


class Biblioteca:
    def __init__(self):
        self.colecao = list()


    def adicionar_livro(self, livro):
        self.colecao.append(livro)


if __name__ == '__main__':


    livro1 = Livro('Dunna', 'Frank Herbert')

    print(f'Livro: {livro1}')

    Colecao = Biblioteca()

    Colecao.adicionar_livro(livro1)


    print(Colecao.colecao[0])