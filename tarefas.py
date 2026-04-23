import json
lista_tarefas = []

def adicionar_tarefa(descricao):
    print("========= ADICIONAR TAREFA ========")
    tarefa = {
        "descricao" :descricao,
        "concluida" : False
    }

    lista_tarefas.append(tarefa)

    
    print("Tarefa adicionada com sucesso!")
    salvar_dados()


def listar_tarefas():

    print("=========== LISTAR TAREFAS ==========")
    for indice, tarefa in enumerate(lista_tarefas):
        if tarefa['concluida'] == True:     
            print(f"{indice}. {tarefa['descricao']} ✅")
        else:
            print(f"{indice}. {tarefa['descricao']} ❌")


def concluir_tarefa(indice):
    print("========= CONCLUIR TAREFA ========")
    try: 
        tarefa = lista_tarefas[indice] 
        if not tarefa['concluida']:
            tarefa['concluida'] = True
            print(f"{indice}. {tarefa['descricao']} ✅ ")
        else: 
            print("Esta tarefa já esta concluida!")
              
    except IndexError:
        print("ERRO: digite um número que esta na lista")


def excluir_tarefa(indice):
   
    print("========= EXCLUIR TAREFA ========")
    try: 
        lista_tarefas[indice] 
        lista_tarefas.pop(indice)
        print("Tarefa excluida")
        salvar_dados()  
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
        
        
