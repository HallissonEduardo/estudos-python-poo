
 
"""
Gerenciador de Tarefas - Padrão MVC em Python.

Este projeto foi desenvolvido para praticar conceitos de Programação Orientada 
a Objetos (POO) e explorar a separação de responsabilidades.

Estrutura da Arquitetura:
- Model: Gerencia os dados e as regras de negócio.
- View: Lida com a exibição de dados e a interação com o usuário.
- Controller: Atua como intermediário e orquestra a aplicação.

Nota de Arquitetura: O Controller conhece e interage com a View e o Model, 
mas Model e View são totalmente independentes e não sabem da existência um do outro.

No repositorio gerenciador-tarefas-mvc  pode ser visto o  desenvolvinento para me aprofundar mais no projeto. 

"""



from controller import TarefaController




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