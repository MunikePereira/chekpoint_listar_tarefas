from tarefas import adicionar_tarefa, listar_tarefas, concluir_tarefa,excluir_tarefa , salvar_dados, carregar_dados
import time

TEMPO = 3
TEMPO_TAREFA = 5
TEMPO_ERRO = 5
carregar_dados()
while True:
    print("============= MENU ============")
    print("||       1. ADICIONAR        ||")
    print("||       2. LISTAR           ||")
    print("||       3. ATUALIZAR LISTA  ||")
    print("||       4. EXCLUIR TAREFA   ||")
    print("||       5. SAIR             ||")

    opcoes = input("Digite uma opção: ")

    match opcoes:
        case "1":
            descricao_usuario = input("Adicione uma descrição: ")
            adicionar_tarefa(descricao_usuario)
            time.sleep(TEMPO)
        
        case "2":
            listar_tarefas()
            time.sleep(TEMPO_TAREFA)
        
        case "3":
            try:
                i = int(input("digite o indice que quer concluir: "))
                concluir_tarefa(i)
                salvar_dados()
            except ValueError:
                print("ERRO: Digite o número inteiro")
            time.sleep(TEMPO)
        case "4":
            try:
                i = int(input("digite o indice que quer concluir: "))
                excluir_tarefa(i)
            except ValueError:
                 print("ERRO: Digite o número inteiro")
            time.sleep(TEMPO)


        case "5":
            print("Fechando programa...")
            time.sleep(TEMPO)
            break

        case _:
            print("Opcão invalída")
            time.sleep(TEMPO_ERRO)


 
    

 
    