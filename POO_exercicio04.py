
"""Criando class generica"""


"""
Desafio 4: Formas Geométricas
O polimorfismo permite tratar objetos de tipos diferentes da mesma maneira,
desde que compartilhem uma estrutura comum.
 """


from typing import Generic,TypeVar

T = TypeVar('T')

class Forma(Generic[T]):

    def __init__(self, altura: float, base: float):
        self.altura = altura
        self.base = base


    def __str__(self):
        return  f"{self.altura}, {self.base}"


    def calcular_area(self):
        raise NotImplementedError



class Retangulo(Forma[T]):

    def calcular_area(self):
        return (self.altura * self.base)


class Circulo(Forma[T]):

    #def __init__(self,base, altura):
        #super().__init__(altura, base)     """Não é necessario colocar o __init__"""

    def calcular_area(self):
        raio = self.altura/2
        return 3.14 * raio**2



if __name__ == '__main__':

    rtq = Retangulo(10,10)
    print(rtq.altura)
    print(rtq.base)
    print(rtq.calcular_area() )

    circulo = Circulo(10,10)
    print(circulo.calcular_area())


    print(circulo)





