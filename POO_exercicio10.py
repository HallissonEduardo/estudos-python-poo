
"""
Desafio 10: O Sistema de Batalha (Interação de Objetos)
"""


class Arma:
    def __init__(self, nome, dano: int):
        self.nome = nome
        self.dano = dano


class Personagem:
    def __init__(self, nome: str, pontos_de_vida: int):
        self.nome = nome
        self.pontos_de_vida = pontos_de_vida
        self.arma_equipada = None

    def equipar(self, arma):

        self.arma_equipada = arma


    def atacar(self, alvo):

        if self.arma_equipada is not None:
            self.dano = self.arma_equipada.dano
            self.nome_arma = self.arma_equipada.nome

        else:
            self.dano = 1
            self.nome_arma = "Mãos nuas"

        alvo.pontos_de_vida -= self.dano

        print(f"{self.nome} atacou {alvo.nome} com {self.nome_arma}!")
        print(f"  -> Causou {self.dano} de dano.")


if __name__ == '__main__':


    arma1 = Arma("125", 12)

    arma2 = Arma("Pistola", 7)

    personagem1 = Personagem("Guilherme", 15)

    personagem1.equipar(arma2)

    personagem2 = Personagem("Matheus", 15)

    personagem2.equipar(arma1)

    personagem2.atacar(personagem1)

    print(f"Agora o {personagem1.nome} tem {personagem1.pontos_de_vida} pontos de vida.")








