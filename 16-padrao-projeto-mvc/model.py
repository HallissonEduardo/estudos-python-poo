from view import TarefaView


# INICIANDO MODEL--------------------------------------------------------------------------------------------------
class TarefaModel:

    """
      Classe TarefaModel: responsável por armazenar, carregar e salvar 
    os dados das tarefas  
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