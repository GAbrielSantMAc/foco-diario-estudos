import json
import os

ARQUIVO_DADOS = "tarefas.json"

def carregar_tarefas():
    if not os.path.exists(ARQUIVO_DADOS):
        return []

    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_tarefas(tarefas):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False)


def adicionar_tarefa(tarefas, nova_tarefa):
    if len(tarefas) >= 3:
        return False, "Limite de 3 tarefas"

    if not nova_tarefa or not nova_tarefa.strip():
        return False, "Tarefa vazia"

    return True, "OK"


def remover_tarefa(tarefas, index):
    try:
        tarefa = tarefas.pop(index)
        return True, tarefa
    except:
        return False, None