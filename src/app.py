import json
import os

ARQUIVO_DADOS = 'tarefas.json'

def carregar_tarefas():
    """Carrega as tarefas salvas no arquivo JSON."""
    if not os.path.exists(ARQUIVO_DADOS):
        return []
    with open(ARQUIVO_DADOS, 'r') as f:
        return json.load(f)

def salvar_tarefas(tarefas):
    """Salva as tarefas no arquivo JSON."""
    with open(ARQUIVO_DADOS, 'w') as f:
        json.dump(tarefas, f)

def adicionar_tarefa(tarefas, nova_tarefa):
    """Regra de Negócio: Adiciona tarefa respeitando o limite de 3 por dia."""
    if len(tarefas) >= 3:
        return False, "Erro: Limite máximo de 3 tarefas atingido! Foco no essencial."
    if not nova_tarefa.strip():
        return False, "Erro: A tarefa não pode ser vazia."
    
    tarefas.append(nova_tarefa.strip())
    return True, "Tarefa adicionada com sucesso!"

def remover_tarefa(tarefas, numero_tarefa):
    """Remove uma tarefa pelo seu número na lista."""
    try:
        indice = numero_tarefa - 1
        if indice < 0:
            raise IndexError
        removida = tarefas.pop(indice)
        return True, f"Parabéns! Tarefa '{removida}' concluída/removida."
    except (IndexError, ValueError):
        return False, "Erro: Número de tarefa inválido."

def iniciar_cli():
    """Interface de Linha de Comando (CLI)."""
    tarefas = carregar_tarefas()
    
    while True:
        print("\n--- 🎯 FOCO DIÁRIO: Organizador de Estudos ---")
        print("1. Adicionar Tarefa de Estudo (Máx: 3)")
        print("2. Listar Tarefas")
        print("3. Concluir/Remover Tarefa")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            nova = input("Digite a tarefa (ex: 'Ler cap 2 de História'): ")
            sucesso, msg = adicionar_tarefa(tarefas, nova)
            print(f"\n> {msg}")
            if sucesso: salvar_tarefas(tarefas)
            
        elif escolha == '2':
            print("\n📋 Suas Tarefas de Hoje:")
            if not tarefas:
                print(" Nenhuma tarefa! Aproveite para descansar ou adicione uma.")
            for i, t in enumerate(tarefas, 1):
                print(f" {i}. {t}")
                
        elif escolha == '3':
            try:
                num = int(input("Digite o número da tarefa concluída: "))
                sucesso, msg = remover_tarefa(tarefas, num)
                print(f"\n> {msg}")
                if sucesso: salvar_tarefas(tarefas)
            except ValueError:
                print("\n> Erro: Digite um número válido.")
                
        elif escolha == '4':
            print("\nAté logo! Mantenha o foco.")
            break
        else:
            print("\n> Opção inválida. Tente novamente.")

# Só roda o menu se o arquivo for executado diretamente (evita rodar no teste)
if __name__ == '__main__':
    iniciar_cli()