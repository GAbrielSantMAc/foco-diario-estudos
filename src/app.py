print("🔥 APP INICIALIZOU")
import os
from flask import Flask, jsonify, request, render_template
from supabase import create_client, Client

app = Flask(__name__)

# -----------------------------
# CONEXÃO COM O SUPABASE
# -----------------------------
# O Render vai ler essas variáveis automaticamente das configurações que você salvou lá
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

# Inicializa o cliente do banco de dados
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


# -----------------------------
# ROTA PRINCIPAL (TESTE)
# -----------------------------
@app.route("/")
def home():
    return jsonify({
        "status": "ok",
        "mensagem": "🔥 Foco Diário conectado ao Supabase e rodando no Render!"
    })


# -----------------------------
# INTERFACE WEB (HTML)
# -----------------------------
@app.route("/app")
def interface():
    return render_template("index.html")


# -----------------------------
# API: LISTAR TAREFAS (SUPABASE)
# -----------------------------
@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    try:
        # Busca todas as tarefas da tabela "tarefas", ordenadas pelo id
        resposta = supabase.table("tarefas").select("*").order("id").execute()
        
        # O Supabase retorna uma lista de dicionários dentro de resposta.data
        # Exemplo: [{"id": 12, "tarefa": "Estudar Geografia"}]
        # Vamos extrair apenas o texto da tarefa para manter a compatibilidade com seu HTML antigo
        lista_formatada = [item["tarefa"] for item in resposta.data]
        
        return jsonify(lista_formatada)
    except Exception as e:
        return jsonify({"sucesso": False, "erro": str(e)}), 500


# -----------------------------
# API: ADICIONAR TAREFA (SUPABASE)
# -----------------------------
@app.route("/tarefas", methods=["POST"])
def adicionar_tarefa():
    data = request.get_json()

    if not data or "tarefa" not in data:
        return jsonify({"sucesso": False, "erro": "Campo 'tarefa' é obrigatório"}), 400

    tarefa_texto = data["tarefa"].strip()

    if not tarefa_texto:
        return jsonify({"sucesso": False, "erro": "Tarefa não pode ser vazia"}), 400

    try:
        # Validação do limite de 3 tarefas direto no banco de dados
        total_atual = supabase.table("tarefas").select("*", count="exact").execute()
        if total_atual.count >= 3:
            return jsonify({"sucesso": False, "erro": "Limite de 3 tarefas atingido"}), 400

        # Insere a nova tarefa na tabela "tarefas" do Supabase
        supabase.table("tarefas").insert({"tarefa": tarefa_texto}).execute()

        return jsonify({"sucesso": True, "mensagem": "Tarefa salva no Supabase com sucesso!"})
    except Exception as e:
        return jsonify({"sucesso": False, "erro": str(e)}), 500


# -----------------------------
# API: REMOVER TAREFA (SUPABASE)
# -----------------------------
@app.route("/tarefas/<int:index>", methods=["DELETE"])
def remover_tarefa(index):
    try:
        # Como o seu HTML trabalha com a posição da lista (0, 1, 2) e não com o ID do banco,
        # precisamos primeiro descobrir qual é o ID real do item que está naquela posição
        resposta = supabase.table("tarefas").select("id").order("id").execute()
        
        if index >= len(resposta.data):
            return jsonify({"sucesso": False, "erro": "Índice inválido"}), 400
        
        # Pega o ID real do banco correspondente à linha clicada
        id_real = resposta.data[index]["id"]

        # Deleta a linha correspondente no Supabase
        supabase.table("tarefas").delete().eq("id", id_real).execute()

        return jsonify({"sucesso": True, "mensagem": "Tarefa removida do banco!"})
    except Exception as e:
        return jsonify({"sucesso": False, "erro": str(e)}), 500


# -----------------------------
# EXECUÇÃO LOCAL
# -----------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)