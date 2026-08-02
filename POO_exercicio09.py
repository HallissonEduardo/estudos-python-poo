
"""
Desafio 9: O Zoológico Seguro (Classes Abstratas)
"""

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def emitir_som(self):
        pass

class Cachorro(Animal):

    def emitir_som(self):
        return 'Au Au'

class Gato(Animal):

    def emitir_som(self):
        return 'Miau Miau'


if __name__ == '__main__':

    Dog = Cachorro()

    print(Dog.emitir_som())

    Cat = Gato()

    print(Cat.emitir_som())

"""
Classes Abstratas: Não permitem a criação de um objeto a partir dela,
é necessario o uso de uma subclass ou classe filha 
"""