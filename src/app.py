print("🔥 APP INICIALIZOU")

import os
from flask import Flask, jsonify, request, render_template
from supabase import create_client, Client

app = Flask(__name__)

# -----------------------------
# CONEXÃO COM SUPABASE
# -----------------------------
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_ANON_KEY")

# segurança (evita crash silencioso no Render)
if not SUPABASE_URL or not SUPABASE_KEY:
    raise Exception("Variáveis do Supabase não carregaram")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


# -----------------------------
# ROTA PRINCIPAL
# -----------------------------
@app.route("/")
def home():
    return jsonify({
        "status": "ok",
        "mensagem": "🔥 Foco Diário rodando no Render + Supabase!"
    })


# -----------------------------
# INTERFACE WEB
# -----------------------------
@app.route("/app")
def interface():
    return render_template("index.html")


# -----------------------------
# LISTAR TAREFAS (SUPABASE)
# -----------------------------
@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    try:
        resposta = supabase.table("tarefas").select("*").order("id").execute()

        # ⚠️ MUDANÇA IMPORTANTE: "titulo"
        lista_formatada = [item["titulo"] for item in resposta.data]

        return jsonify(lista_formatada)

    except Exception as e:
        return jsonify({"sucesso": False, "erro": str(e)}), 500


# -----------------------------
# ADICIONAR TAREFA
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
        # limite de 3 tarefas
        total_atual = supabase.table("tarefas").select("*", count="exact").execute()

        if total_atual.count >= 3:
            return jsonify({"sucesso": False, "erro": "Limite de 3 tarefas atingido"}), 400

        # ⚠️ MUDANÇA IMPORTANTE: "titulo"
        supabase.table("tarefas").insert({
            "titulo": tarefa_texto,
            "concluida": False
        }).execute()

        return jsonify({"sucesso": True, "mensagem": "Tarefa salva no Supabase!"})

    except Exception as e:
        return jsonify({"sucesso": False, "erro": str(e)}), 500


# -----------------------------
# REMOVER TAREFA
# -----------------------------
@app.route("/tarefas/<int:index>", methods=["DELETE"])
def remover_tarefa(index):
    try:
        resposta = supabase.table("tarefas").select("id").order("id").execute()

        if index >= len(resposta.data):
            return jsonify({"sucesso": False, "erro": "Índice inválido"}), 400

        id_real = resposta.data[index]["id"]

        supabase.table("tarefas").delete().eq("id", id_real).execute()

        return jsonify({"sucesso": True, "mensagem": "Tarefa removida!"})

    except Exception as e:
        return jsonify({"sucesso": False, "erro": str(e)}), 500


# -----------------------------
# EXECUÇÃO LOCAL / RENDER
# -----------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)