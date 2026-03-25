import sys
import os

# Esse truque ajuda o Python a encontrar a nossa pasta 'src' para testar o app.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app import adicionar_tarefa, remover_tarefa

# 1. Teste de Caminho Feliz (Uso correto)
def test_adicionar_tarefa_sucesso():
    tarefas = []
    sucesso, msg = adicionar_tarefa(tarefas, "Estudar Matemática")
    assert sucesso is True
    assert len(tarefas) == 1
    assert tarefas[0] == "Estudar Matemática"

# 2. Teste de Caso Limite (Regra das 3 tarefas)
def test_adicionar_tarefa_limite_maximo():
    tarefas = ["História", "Física", "Química"] # Já tem 3
    sucesso, msg = adicionar_tarefa(tarefas, "Biologia") # Tentando a 4ª
    assert sucesso is False
    assert "Limite máximo" in msg
    assert len(tarefas) == 3 # A lista tem que continuar com 3

# 3. Teste de Entrada Inválida (Tarefa Vazia)
def test_adicionar_tarefa_vazia():
    tarefas = []
    sucesso, msg = adicionar_tarefa(tarefas, "   ") # Espaços em branco
    assert sucesso is False
    assert "não pode ser vazia" in msg
    assert len(tarefas) == 0

# 4. Teste de Comportamento Indevido (Remover tarefa que não existe)
def test_remover_tarefa_invalida():
    tarefas = ["Estudar Python"]
    sucesso, msg = remover_tarefa(tarefas, 5) # Tentando remover a tarefa número 5
    assert sucesso is False
    assert "inválido" in msg
    assert len(tarefas) == 1