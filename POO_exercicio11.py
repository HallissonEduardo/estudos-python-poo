"""
Desafio 11: Criar uma classe que reconhece se o dia do mês é quarta-feira se for tem que usar rosa
"""


import datetime

class Dia_rosa:
    def __init__(self):
        #self.dia_atual = datetime.date.today()
        self.dia_semana:int = datetime.date.weekday(datetime.date.today())
        self.day_weekday:list = ["Segunda-feira", "Terça-feira", "Quarta-feira",
                            "Quinta-feira", "Sexta-feira", "Sabado", "Domingo"]


    def criar_rosa(self):
        if self.dia_semana == 2:
            return f"Hoje é quarta feira devemos usar rosa!"

        elif (self.dia_semana == 4) or (self.dia_semana == 5) or (self.dia_semana == 6 ):
            return f"Hoje não é quarta feira! Hoje é {self.day_weekday[self.dia_semana]} Bom fim de semana!"


        else:
            return f"Hoje não é quarta feira! Hoje é {self.day_weekday[self.dia_semana]} Boa semana"


"""if __name__ == "__main__":

    rosa = Dia_rosa()

    print(rosa.dia_semana)

    print(rosa.criar_rosa())
"""

# Desafio com get e setter ----------------------------------------------


#-------------------------------------------------

class Day_of_pink:

    day_pink = "Quarta"


    def __int__(self, day):
        self._day = day



    @property
    def today(self):
            return self._day

    @today.setter
    def today(self, new_day):

        if not isinstance(new_day,str):
            raise TypeError

        if new_day not in self.day_pink:

            raise ValueError (f"{new_day} is not a pink day")

        else:
            self._day = "Today is a pink day! please wear a shirt pink"



"""if __name__ == "__main__":

    calendar = Day_of_pink()
    calendar.today = "Quarta"
    print(calendar.today)"""

#-------------------------------------------------------------------------



# Validação usando case -------------------------------------------------------------


class Day:


    def __init__(self):
        self._day = None

    @property
    def today(self):
        return self._day

    @today.setter
    def today(self, new_day):

        match new_day:

            case "Quarta":
                self._day = "Hoje é quarta feira devemos usar rosa!"

            case "Sexta"|"Sabado"|"Domingo":
                self._day = "Hoje não é quarta feira, mas é final de semana, bom fim de semana!"

            case _:
                self._day = "Hoje não é quarta feira não devemos usar rosa!"


if __name__ == "__main__":

    calendario = Day()
    calendario.today = "Quarta"
    print(calendario.today)













