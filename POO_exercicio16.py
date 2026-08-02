"""
Gerenciador de Tarefas

Seu programa deve permitir ao usuário:

Adicionar uma nova tarefa.

Listar todas as tarefas pendentes e concluídas. Model

Marcar uma tarefa como concluída.

Sair do programa.

Projeto desenvolvido para aplicar o conceito MVC. Model, View e Controller.
"""

# INICIANDO MODEL--------------------------------------------------------------------------------------------------
class TarefaModel:

    """
Essa é a classe do TarefaModel, tem o objetivo e apenas armazenar os dados fornecidos na classe TarefaView;
e passados pela classe TarefaController.
    """

    def __init__(self):
        self.tarefas_pendentes: list = []   # CRIEI DUAS LISTAS A PRIMEIRA CONTEM AS TAREFAS PENDENTES.
        self.tarefas_concluidas: list = [] # A SEGUNDA CONTEM TODAS AS TAREFAS CONCLUIDAS.


    def adicionar_pendentes(self,tarefa):
        self.tarefa_limpa = tarefa # RECEBE A TAREFA PENDENTE PASSADA NO PELA CLASSE VIEW E ENTREGUE PELO CONTROLLER

        if not self.tarefa_limpa: # VALIDA SE TAREFA EXISTE
            return False

        self.tarefas_pendentes.append(self.tarefa_limpa) # ADICIONA TAREFA A LISTA TAREFAS_PENDENTES.


    def tarefa_concluida(self, concluir_tarefa):
        self.concluir_tarefa = concluir_tarefa # RECEBE A TAREFA QUE FICARA COMO CONCLUIDA

        if not self.concluir_tarefa: # VALIDA SE TAREFA EXISTE
            return False

        if self.concluir_tarefa in self.tarefas_pendentes: # VALIDA SE A TAREFA JA EXISTE NA LISTA DE PENDENTES.
            self.tarefas_pendentes.remove(self.concluir_tarefa) # SE SIM, REMOVE ELA E EM SEGUIDA A ADICIONA NA LISTA DE CONCLUIDOS.

        self.tarefas_concluidas.append(self.concluir_tarefa)


    def dicionario_tarefas(self)->dict:
         dados = {
            "Tarefas Pendentes": self.tarefas_pendentes,
            "Tarefas Concluidas": self.tarefas_concluidas
        }

         return dados # RETORNA OS DADOS DAS DUAS LISTAS SALVAS EM UM DICIONARIO.


# Finalizando Model--------------------------------------------------

# INICIANDO VIEW--------------------------------------------------------------------


class TarefaView:

    """
Essa classe é a TarefaView e responsavel exclusivamente por mustra informacoes processadas pelo Controlller,
contem apenas input e return
    """

    def __init__(self):
        """self.controle = controle"""


    def interface(self):
        print("--Gerenciador De Tarefas---")
        print("1-Adicionar Tarefa")
        print("2-Listar Tarefas")
        print("3-Concluir Tarefas")
        print("4-Sair")


    def pedir_dados(self, mensagem)->None:
        return input(mensagem).strip() # RETORNA O INPUT QUE RETORNA


    def exibir_mensagem(self, msg)->str:
        return input(msg).strip()


    def adicionar_texto_tarefa(self, mensagem)->str:
        return input(mensagem).strip()

    def msg_pendente(self, msg)->None:
        return msg

    def listar_tarefas(self, pendentes, concluidas):
    # LISTA TODAS AS TAREFAS ARMAZENADAS NO MODEL E PROCESSAS E ENTREGUES PELO CONTROLLER.

        print("\nTarefas Pendentes:")

        if not pendentes: # VALIDA SE EXISTE TAREFAS PENDENTES
            print("\nNão tem tarefas pendentes")

        else:
            
            for pendente in pendentes: # LAÇO DE REPETIÇÃO "FOR" PERCORRE A LISTA DE PENDENTES E RETORNA A LISTA
                print(pendente)

        print("\nTarefas Concluidas:")

        if not concluidas:
            print("\nNão tem tarefas concluidas")

        else:
            for concluida in concluidas:
                print(concluida)

# FINALIZANDO VIEW------------------------------------------------------------------------

# INICIANDO CONTROLLER ------------------------------------------------------------

class TarefaController:

    """
Classe TarefaController responsavel por processar os dados, e fazer a ligação entre Model e View.
    """

    def __init__(self):
        self.model = TarefaModel()
        self.view = TarefaView()


    def dicionario(self):
        self.listas = self.model.dicionario_tarefas()
        return self.listas


    def iniciar(self):

        while True:

            self.view.interface()
            self.opcao = self.view.pedir_dados("\nDigite o número referente a opção desejada:")


            match self.opcao:

                case "1":

                    self.novo_tarefa = self.view.adicionar_texto_tarefa("\nQual tarefa quer adicionar:")

                    if self.novo_tarefa:
                        self.model.adicionar_pendentes(self.novo_tarefa)
                        self.view.exibir_mensagem("\nTarefa adicionada com sucesso")

                case "2":

                    dados = self.model.dicionario_tarefas()

                    lista_pendentes = dados["Tarefas Pendentes"]

                    lista_concluidas = dados["Tarefas Concluidas"]

                    self.view.listar_tarefas(lista_pendentes, lista_concluidas)

                    self.view.exibir_mensagem("\nLista Carregada com sucesso ")

                case "3":

                    self.concluir_tarefa = self.view.adicionar_texto_tarefa("\nQual tarefa quer marcar como concluida:")

                    if self.concluir_tarefa:
                        self.model.tarefa_concluida(self.concluir_tarefa)
                        self.view.exibir_mensagem("\nTarefa concluida com sucesso")

                case "4":
                    self.view.exibir_mensagem("\n Saindo do Gerenciador de Tarefas")
                    return False

                case _:
                    self.view.exibir_mensagem("Valor invalido")



if __name__ == '__main__':

    app = TarefaController()
    app.iniciar()




    """lista_tarefas = TarefaModel()
    lista_tarefas.adicionar_pendentes("A")
    print(lista_tarefas.tarefas_pendentes)
    lista_tarefas.adicionar_pendentes("B")
    lista_tarefas.adicionar_pendentes("C")
    lista_tarefas.tarefa_concluida("C")
    print(lista_tarefas.tarefas_pendentes)
    print(lista_tarefas.tarefas_concluidas)
    print(lista_tarefas.listar_tarefas())"""



    '''model = TarefaModel()
    view = TarefaView(model)
    model.adicionar_pendentes("A")
    model.adicionar_pendentes("B")

    view.interface()
    view.listar_tarefas(model)'''



    """model = TarefaModel()

    # 2. Injetamos o Modelo na View
    view = TarefaView(model)

    controller = TarefaController(view, model)

    # 3. Adicionamos dados no modelo
    model.adicionar_pendentes("Estudar Injeção de Dependências")
    model.adicionar_pendentes("Fazer o projeto principal")

    # Marcamos a primeira como concluída para testar a lógica
    model.tarefa_concluida("Estudar Injeção de Dependências")

    # 4. Usamos a View para exibir os dados do Modelo
    view.interface()
    view.listar_tarefas()"""



























