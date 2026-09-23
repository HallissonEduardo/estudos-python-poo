

"""
Desafio 15: O Super-Herói (Herança Múltipla)
Python é uma das poucas linguagens modernas que permite que uma classe tenha mais de uma classe mãe.
Chamamos isso de Herança Múltipla.
"""


"""
Objetivo: Combinar comportamentos de diferentes famílias de classes.

Requisitos:

Crie uma classe Voador com um método voar().

Crie uma classe Nadador com um método nadar().

Crie uma classe SuperHeroi que herda de ambas (class SuperHeroi(Voador, Nadador):).

Instancie o super-herói e chame os dois métodos para provar que ele herdou ambas as habilidades.

"""




class Voador:

# Criei métodos contrutor com dois atributos que serão herdados da classe filha.
# A baixo temos dois métodos para herança da classe filha.

    def __init__(self):
        self.voando = False
        self.altura: float = 0.0

    def voar(self, altura: float):
        self.voando = True
        self.altura = altura


    def descer(self):
        if self.voando:
            self.voando = False
            self.altura = 0.0




class Nadador:

# Da mesma forma que a classe anterior criamos um método contrutor com dois atributos que serão herdados pela classe filha.
# Depois dois métodos com o mesmo intuito

    def __int__(self):
        self.nadando = False
        self.profundidade: float= 0.0


    def nadar(self, profundidade: float):
        self.nadando = True
        self.profundidade = profundidade


    def emergir(self):
        if self.nadando:
            self.nadando = False





class SuperHeroi(Voador, Nadador):
# Quando adicionamos (Voador, Nadador) estamos chamando as classes mãe para dentro da classe filha.

    def __init__(self):
        Voador.__init__(self)# Chamamos os atributos das classes mãe.
        Nadador.__init__(self)


    # Adicionamos validações nos métodos já criados nas classes.

    def voar(self, altura):

        if self.nadando:
            print('Não pode nadar e voar ao mesmo tempo!')

        else:
            super().voar(altura) # Atualizando atributos.

    def nadar(self, profundidade):
        if self.voando:
            print("Não pode nadar e voar ao mesmo tempo!")

        else:
            super().nadar(profundidade) # Atualizando atributos.





if __name__ == '__main__':

    """
    Instanciando métodos da classe Nadador.
    """

    try:# Para deixar o erro explicito se aconteçer.

        Capitao_patria = SuperHeroi()

        nd: float = input("Quanto você quer descer:")

        Capitao_patria.nadar(nd)

        print(f"Capitão pátria está nadando a {Capitao_patria.profundidade} metros")

        Capitao_patria.emergir()


#Instanciando métodos da classe Voador.


        vr: float = input("Quanto você quer subir:")

        Capitao_patria.voar(vr)

        print(f"Capitão pátria esta voando a {Capitao_patria.altura} metros")

        Capitao_patria.descer()

    except Exception as erro:
        print(erro)














