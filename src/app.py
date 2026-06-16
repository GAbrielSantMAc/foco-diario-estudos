from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# -----------------------------
# DADOS EM MEMÓRIA (FALLBACK)
# -----------------------------
tarefas = []


# -----------------------------
# ROTA PRINCIPAL
# -----------------------------
@app.route("/")
def home():
    return jsonify({
        "status": "ok",
        "mensagem": "🔥 Foco Diário rodando no deploy!"
    })


# -----------------------------
# LISTAR TAREFAS
# -----------------------------
@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    return jsonify(tarefas)


# -----------------------------
# ADICIONAR TAREFA
# -----------------------------
@app.route("/tarefas", methods=["POST"])
def adicionar_tarefa():
    data = request.get_json()

    if not data or "tarefa" not in data:
        return jsonify({
            "sucesso": False,
            "erro": "Campo 'tarefa' é obrigatório"
        }), 400

    tarefa = data["tarefa"].strip()

    if not tarefa:
        return jsonify({
            "sucesso": False,
            "erro": "Tarefa não pode ser vazia"
        }), 400

    if len(tarefas) >= 3:
        return jsonify({
            "sucesso": False,
            "erro": "Limite de 3 tarefas atingido"
        }), 400

    tarefas.append(tarefa)

    return jsonify({
        "sucesso": True,
        "mensagem": "Tarefa adicionada com sucesso!",
        "tarefas": tarefas
    })


# -----------------------------
# REMOVER TAREFA
# -----------------------------
@app.route("/tarefas/<int:index>", methods=["DELETE"])
def remover_tarefa(index):
    try:
        removida = tarefas.pop(index)
        return jsonify({
            "sucesso": True,
            "removida": removida,
            "tarefas": tarefas
        })
    except IndexError:
        return jsonify({
            "sucesso": False,
            "erro": "Índice inválido"
        }), 400


# -----------------------------
# START LOCAL (IGNORADO NO RENDER)
# -----------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)