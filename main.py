from tarefas import adicionar_tarefa, listar_tarefas
import time

TEMPO = 10
TEMPO_TAREFA = 15
TEMPO_ERRO = 5

while True:
    print("============= MENU ============")
    print("||       1. ADICIONAR        ||")
    print("||       2. LISTAR           ||")
    print("||       3. SAIR             ||")

    opcoes = input("Digite uma opção: ")

    match opcoes:
        case "1":
            descricao_usuario = input("Adicione uma descrição: ")
            adicionar_tarefa(descricao_usuario)
        
        case "2":
            listar_tarefas()
            time.sleep(TEMPO_TAREFA)

        case "3":
            print("Fechando programa...")
            time.sleep(TEMPO)
            break

        case _:
            print("Opcão invalída")
            time.sleep(TEMPO_ERRO)


 
    