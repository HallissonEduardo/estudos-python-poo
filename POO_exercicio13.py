"""
Múltiplas Formas de Nascer (Métodos de Classe)
Objetivo: Diferenciar o self (instância) do cls (classe).
"""

"""
Um exemplo pratico de como aplicar o método decorador @classmethod para instanciar a classe dentro de si,
usando a classe (cls) para criar e devolver uma nova instância (um novo objeto) com seus próprios atributos de instância (c_data.dia).
"""

"""
O porquê: Isso evita que o desenvolvedor que usa sua classe precise tratar a string no código dele. 
A própria classe ensina como se construir a partir de um texto.
"""

#---------------------------------------------------------------------------------------------------------------------

class Data:

    #   Atualmente, o __init__ não recebe nada e cria um objeto vazio (None). Depois, o método de_string preenche.
    def __init__(self):
        self.dia = None
        self.mes = None
        self.ano = None


    @classmethod
    def de_string(cls,data_str:str): # Vai receber uma str no formato DD-MM-YYYY

        try:
            c_data = cls() # Importante lembrar de instanciar a classe dentro de si usando o cls()

            dia, mes, ano = data_str.strip().split("-") # Usando o split() para separar uma str em partes
                                                        # antes "19-11-2000"
            c_data.dia = int(dia)                       # depois 19, 11, 2000
            c_data.mes = int(mes)
            c_data.ano = int(ano)

            # O c_data esta servindo para instanciar a classe e chamar para chamar os atributos, depois é armazenado o novo valor

            # Aqui armazenamos os valores nos atributos dia, mes, ano

            # Deixamos explicito que o valores serão inteiros, fazendo uma conversão

            return c_data
            # retorna as modificações feitas na class

        # Caso o usuário digite letras ou no formato errado (ex: 19/11/2000)
        except ValueError:
            print("Valor invalido")
            return None

#------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # Variavel que recebe a data do usuario
    get = input("Digite a data:")

    # Instanciando a classe Data na variavel data,
    # depois chamamos a função de_string para processamento do valor na variavel get
    data = Data.de_string(get)

    # Visualização do dia, mes e ano
    if data is not None:
        print(f"Dia:{data.dia}")
        print(f"Mês:{data.mes}")
        print(f"Ano:{data.ano}")

#---------------------------------------------------------------------------------------------

"""
Nesse projeto aplico fundamentos de Herança.
O cls refere-se à subclasse que chamou o método (polimorfismo).
"""