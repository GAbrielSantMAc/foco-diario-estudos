from app_cli import carregar_tarefas, adicionar_tarefa, remover_tarefa

def iniciar_cli():
    tarefas = carregar_tarefas()

    while True:
        print("\n1 - Adicionar")
        print("2 - Listar")
        print("3 - Remover")
        print("4 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            nova = input("Tarefa: ")
            adicionar_tarefa(tarefas, nova)

        elif opcao == "2":
            print(tarefas)

        elif opcao == "3":
            i = int(input("Índice: "))
            remover_tarefa(tarefas, i)

        elif opcao == "4":
            break

if __name__ == "__main__":
    iniciar_cli()