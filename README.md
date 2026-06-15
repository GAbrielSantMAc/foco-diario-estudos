## 🌐 Deploy
Aplicação publicada: https://gabrielsantmac.github.io/foco-diario-estudos/

---# 🎯 Foco Diário: Organizador de Estudos CLI

**Versão Atual:** `1.0.0`

## 📖 Sobre o Projeto (O Problema e a Solução)

**Qual problema estou tentando resolver?**
Muitos estudantes, especialmente pessoas neurodivergentes (com TDAH, por exemplo) ou que sofrem com ansiedade, sentem uma forte "sobrecarga mental" (paralisia por análise) ao se depararem com listas de estudos gigantescas. Isso gera procrastinação e frustração.

**Como a aplicação ajuda?**
O **Foco Diário** é uma aplicação simples de Linha de Comando (CLI) que atua como um organizador minimalista. A regra de ouro do sistema é: **o usuário só pode cadastrar no máximo 3 tarefas de estudo por dia.** Isso força a priorização do que é realmente essencial, quebra a sobrecarga cognitiva e traz uma sensação de dever cumprido mais rápida.

**Público-alvo:** Estudantes, concurseiros, universitários e pessoas neurodivergentes com dificuldade em manter uma rotina de estudos estruturada.

---

## Tecnologias Utilizadas

- Python 3.11
- Requests
- Pytest
- Supabase
- GitHub Actions

## Banco de Dados

O projeto utiliza Supabase (PostgreSQL em nuvem) para armazenamento persistente das tarefas.

## Funcionalidades

- Adicionar tarefas
- Remover tarefas
- Limite de 3 tarefas diárias
- Frases motivacionais via API ZenQuotes
- Persistência de dados em banco de dados Supabase

## Qualidade

- Testes automatizados com Pytest
- Integração contínua com GitHub Actions
