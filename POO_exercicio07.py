
"""
Desafio 7: O Termostato (Usando @property)
Em linguagens como Java, é comum criar métodos como get_temperatura() e set_temperatura().
Em Python, nós usamos "Properties" para fazer isso de forma mais elegante,
permitindo tratar um método como se fosse um atributo simples, mas mantendo a segurança.
"""

class Termostato:
    def __init__(self):
        self._temperatura = 20

    @property
    def temperatura(self):

        # O property transforma o método em um "Getter"

        return self._temperatura

    # O .setter permite validar o dado antes de salvar
    @temperatura.setter
    def temperatura(self, nov_temp: int):

       if 0 <= nov_temp <= 60:
            self._temperatura = nov_temp


#  Criando sem o metodo property-----------------------------


class Term:
    def __init__(self):
        self._temp = 20


    def get_temperatura(self):
        return self._temp


    def set_temperatura(self, temp: int):
        if 0 <= temp <= 60:
            self._temp = temp




if __name__ == '__main__':


    tp = Term()
    print(tp.get_temperatura())

    tp.set_temperatura(25)
    print(tp.get_temperatura())





"""term= Termostato()
    term.temperatura = 1
    print(term.temperatura)"""


    #Praticar essa metodologia de organização

#---------------------------------------------------------
    # Pascal case
    # getTemp

    #Camel Case
    #GetTemp

    #sneak case
    # get_temp

#----------------------------------------------------------















