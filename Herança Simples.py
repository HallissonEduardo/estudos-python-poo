
"""Desafio 3: O Sistema da Empresa"""

"""Criando classe  Funcionario que gerencia os funcionaripos de uma empresa hipotetica"""


class Funcionario: # Método contrutor

    def __init__(self,nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentar_salario(self, aumento):

        if aumento:
            self.salario += aumento

    def exibir_dados(self):
        print(f'Nome do Funcionario: {self.nome}, Salario: {self.salario}')



# Classe filha da classe Funcionario
class Gerente(Funcionario):

    def __init__(self,nome,salario, setor):
        super().__init__(nome, salario)
        self.setor: str = setor


    def exibir_dados(self):
        print(f'Nome do Gerente: {self.nome}, Salario: {self.salario}, Setor: {self.setor}')




if __name__ == '__main__':

    funcionario1 = Funcionario('Maria', 2000)
    gerente1 = Gerente('Marcia', 2000, setor='TI')
    funcionario1.exibir_dados()
    gerente1.exibir_dados()

    """funcionario1 = Funcionario('Maria', 2000)

    funcionario1.exibir_dados()

    funcionario1.aumentar_salario(200)

    funcionario1.exibir_dados()"""









