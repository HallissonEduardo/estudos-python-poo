from controller import TarefaController





class TarefaView:

    """
       Classe responsável exclusivamente pela interação com o usuário (CLI).
    Exibe os menus e captura as escolhas do usuário de forma totalmente isolada, 
    sem conhecimento da existência do TarefaModel ou do TarefaController.
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

