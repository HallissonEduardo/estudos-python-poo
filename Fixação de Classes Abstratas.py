"""
Exercicio para fixar o conceito de classe abstrata,
Não é possivel criar um objeto dela, uma classe filha e obrigada a ter os métodos pré-definidos da classe.
"""


from abc import ABC, abstractmethod # A IMPORTAÇÃO DA BIBLIOTECA ABC É NECESSARIA PARA CRIAR UMA CLASSSE ABSTRATA NO PYTHON

class Ligar(ABC):
    @abstractmethod
    def ligar(self):
        pass


class Controle(Ligar):

    def ligar(self):
        print("ligando, ar-condicionado")

    def temperatura(self, temperatura):
        temperatura = temperatura

        if temperatura > 100:
            print("temperatura > 100, vai morrer queimado")

        print( f"{temperatura}")


if __name__ == "__main__":
    ligar = Controle()
    ligar.ligar()
    ligar.temperatura(10)
    ligar.temperatura(20)