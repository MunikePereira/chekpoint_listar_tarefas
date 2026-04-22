import json
lista_tarefas = []

def adicionar_tarefa(descricao):
    tarefa = {
        "descricao" :descricao,
        "concluida" : False
    }

    lista_tarefas.append(tarefa)

    salvar_dados()
    print("Tarefa adicionada com sucesso!")
     



def listar_tarefas():

    print("=========== LISTAR TAREFAS ==========")
    for indice, tarefa in enumerate(lista_tarefas):
        if tarefa['concluida'] == True:     
            print(f"{indice}. {tarefa['descricao']} ✅")
        else:
            print(f"{indice}. {tarefa['descricao']} ❌")

def concluir_tarefa(indice):
   
    try: 
        tarefa = lista_tarefas[indice] 
        if not tarefa['concluida']:
            tarefa['concluida'] = True
            print(f"{indice}. {tarefa['descricao']} ✅ ")
        else: 
            print("Está tarefa ja esta concluida")
    except TypeError:
        print("ERRO: Digite o número inteiro")
    except IndexError:
        print("ERRO: digite um número que esta na lista")


def salvar_dados():
    global lista_tarefas
    with open(".\\checkpoint\chekpoint_listar_tarefas\dados.json", "w") as arquivo:
        json.dump(lista_tarefas, arquivo)
        print("Dados salvo com sucesso!")


def carregar_dados():
        global lista_tarefas
        try:
            with open(".\\checkpoint\\chekpoint_listar_tarefas\\dados.json", "r") as arquivo:
               lista_tarefas = json.load(arquivo)
               print("Dados carregando...😊")
            
        except FileNotFoundError:
            print("Nenhum dado. \n Iniciando!...")
            lista_tarefas = []
        
        
