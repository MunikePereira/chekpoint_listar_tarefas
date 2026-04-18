lista_tarefas = []

def adicionar_tarefa(descricao):
    tarefa = {
        "descricao" :descricao,
        "concluida" : False
    }

    lista_tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

    return descricao 



def listar_tarefas():

    print("=========== LISTAR TAREFAS ==========")
    for tarefa in lista_tarefas:
        if tarefa['concluida'] == True:     
            print(f"{tarefa['descricao']} ✅")
        else:
            print(f"{tarefa['descricao']} ❌")

def concluir_tarefa(indice):
    print("Deseja")
        
        


