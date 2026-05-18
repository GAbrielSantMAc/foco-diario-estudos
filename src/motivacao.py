import requests

def buscar_frase_motivacional():
    """Busca uma frase motivacional da API ZenQuotes."""
    try:
        resposta = requests.get("https://zenquotes.io/api/today", timeout=5)
        resposta.raise_for_status()
        dados = resposta.json()
        frase = dados[0]['q']
        autor = dados[0]['a']
        return f'💡 "{frase}" — {autor}'
    except Exception:
        return '💡 "Foco no que importa. Um passo de cada vez."'