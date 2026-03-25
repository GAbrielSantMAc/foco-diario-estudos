# 🎯 Foco Diário: Organizador de Estudos CLI

**Versão Atual:** `1.0.0`

## 📖 Sobre o Projeto (O Problema e a Solução)

**Qual problema estou tentando resolver?**
Muitos estudantes, especialmente pessoas neurodivergentes (com TDAH, por exemplo) ou que sofrem com ansiedade, sentem uma forte "sobrecarga mental" (paralisia por análise) ao se depararem com listas de estudos gigantescas. Isso gera procrastinação e frustração.

**Como a aplicação ajuda?**
O **Foco Diário** é uma aplicação simples de Linha de Comando (CLI) que atua como um organizador minimalista. A regra de ouro do sistema é: **o usuário só pode cadastrar no máximo 3 tarefas de estudo por dia.** Isso força a priorização do que é realmente essencial, quebra a sobrecarga cognitiva e traz uma sensação de dever cumprido mais rápida.

**Público-alvo:** Estudantes, concurseiros, universitários e pessoas neurodivergentes com dificuldade em manter uma rotina de estudos estruturada.

---

## ⚙️ Funcionalidades Principais

* **Adicionar Tarefa:** Insere uma nova meta de estudo (limitado a 3 ativas por vez).
* **Listar Tarefas:** Mostra as tarefas focais do dia.
* **Concluir/Remover Tarefa:** Remove a tarefa da lista após a conclusão.
* **Persistência de Dados:** As tarefas são salvas automaticamente em um arquivo `tarefas.json`, garantindo que não se percam ao fechar o terminal.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Interface:** CLI (Command Line Interface)
* **Testes Automatizados:** `pytest`
* **Análise Estática (Linting):** `flake8`
* **CI/CD:** GitHub Actions (Pipeline automatizada configurada em `.github/workflows/ci.yml`)
* **Dependências:** Declaradas no arquivo `requirements.txt`

---

## 🚀 Como Instalar e Executar

**1. Clone este repositório:**
```bash
git clone [https://github.com/SEU_USUARIO/foco-diario-estudos.git](https://github.com/GAbrielSantMAc/foco-diario-estudos.git)
cd foco-diario-estudos
