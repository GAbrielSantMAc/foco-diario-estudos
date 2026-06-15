import json
import os

from motivacao import buscar_frase_motivacional
from supabase_db import carregar_tarefas_supabase, adicionar_tarefa_supabase

ARQUIVO_DADOS = "tarefas.json"


def carregar_tarefas():
    """Carrega tarefas do JSON local."""
    if not os.path.exists(ARQUIVO_DADOS):
        return []

    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_tarefas(tarefas):
    """Salva tarefas no JSON local."""
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False)


def adicionar_tarefa(tarefas, nova_tarefa):
    """Regra de negócio: máximo de 3 tarefas."""
    if len(tarefas) >= 3:
        return False, "Erro: Limite máximo de 3 tarefas atingido!"

    if not nova_tarefa.strip():
        return False, "Erro: A tarefa não pode ser vazia."

    tarefas.append(nova_tarefa.strip())
    return True, "Tarefa adicionada com sucesso!"


def remover_tarefa(tarefas, numero_tarefa):
    """Remove tarefa pelo índice."""
    try:
        indice = numero_tarefa - 1

        if indice < 0:
            raise IndexError

        removida = tarefas.pop(indice)

        return True, f"Parabéns! Tarefa '{removida}' concluída/removida."

    except (IndexError, ValueError):
        return False, "Erro: Número de tarefa inválido."


def iniciar_cli():
    """Interface de Linha de Comando."""

    try:
        dados = carregar_tarefas_supabase()
        tarefas = [t["titulo"] for t in dados]
    except Exception:
        tarefas = carregar_tarefas()

    print(buscar_frase_motivacional())

    while True:
        print("\n--- 🎯 FOCO DIÁRIO: Organizador de Estudos ---")
        print("1. Adicionar Tarefa de Estudo (Máx: 3)")
        print("2. Listar Tarefas")
        print("3. Concluir/Remover Tarefa")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nova = input(
                "Digite a tarefa (ex: 'Ler capítulo 2 de História'): "
            )

            sucesso, msg = adicionar_tarefa(tarefas, nova)

            print(f"\n> {msg}")

            if sucesso:
                try:
                    adicionar_tarefa_supabase(nova)
                except Exception:
                    salvar_tarefas(tarefas)

        elif escolha == "2":
            print("\n📋 Suas Tarefas de Hoje:")

            if not tarefas:
                print(" Nenhuma tarefa cadastrada.")

            for i, tarefa in enumerate(tarefas, start=1):
                print(f" {i}. {tarefa}")

        elif escolha == "3":
            try:
                num = int(
                    input("Digite o número da tarefa concluída: ")
                )

                sucesso, msg = remover_tarefa(tarefas, num)

                print(f"\n> {msg}")

                if sucesso:
                    salvar_tarefas(tarefas)

            except ValueError:
                print("\n> Erro: Digite um número válido.")

        elif escolha == "4":
            print("\nAté logo! Mantenha o foco.")
            break

        else:
            print("\n> Opção inválida. Tente novamente.")


if __name__ == "__main__":
    iniciar_cli()