
"""
Desafio 6: O Contador de Funcionários (Variáveis de Classe)
Até agora, os atributos pertenciam a cada cópia (instância) do objeto.
Mas e se a própria classe precisar guardar uma informação compartilhada por todos?
"""

class Funcionario:
    def __init__(self):
        self.Total_funcionario = 0

    def Novo_funcionario(self, nome, sertor):
        self.Total_funcionario += 1
        self.nome = nome
        self.sertor = sertor

    def informar_funcionario(self):
        return self.nome, self.sertor



if __name__ == '__main__':

    funcionario = Funcionario()

    funcionario.Novo_funcionario('hallisson', 'TI')

    print(funcionario.Total_funcionario)

    print(funcionario.informar_funcionario())
