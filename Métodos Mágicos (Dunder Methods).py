
"""
Desafio 8: O Carrinho de Compras (Métodos Mágicos)
Agora vamos ensinar o Python a usar a função nativa len() no seu próprio objeto.
"""



class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f'Produto: {self.nome}-R${self.preco}'


class Carrinho:
    def __init__(self):
        self.itens = list()

    def __str__(self):
        return f'Carrinho: {self.itens}'

    def __len__(self):
        return len(self.itens)

    def adicionar_itens(self, itens: list):
        self.itens = itens


if __name__ == '__main__':

    produto1 = Produto('livro', 12.00)
    print(produto1)

    produto2 =  Produto('celular', 12.00)

    print(produto2)

    meu_carrinho = Carrinho()

    meu_carrinho.adicionar_itens([produto1, produto2])

    print(len(meu_carrinho))