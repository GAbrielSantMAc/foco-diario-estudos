import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

url = os.getenv("https://bhumdpghnebfkyowaego.supabase.co")
key = os.getenv("sb_publishable_mkXR4hH6Dt46GGNyi2LIsw_RyXoO8jQ")

supabase = create_client(url, key)

def carregar_tarefas_supabase():
    resposta = supabase.table("tarefas").select("*").execute()
    return resposta.data

def adicionar_tarefa_supabase(titulo):
    supabase.table("tarefas").insert({
        "titulo": titulo,
        "concluida": False
    }).execute()

def remover_tarefa_supabase(id_tarefa):
    supabase.table("tarefas").delete().eq("id", id_tarefa).execute()