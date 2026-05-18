from unittest.mock import patch, MagicMock
from src.motivacao import buscar_frase_motivacional


def test_frase_motivacional_com_sucesso():
    """Testa se a função processa corretamente a resposta da API."""
    resposta_falsa = MagicMock()
    resposta_falsa.status_code = 200
    resposta_falsa.json.return_value = [
        {"q": "Acredite em você.", "a": "Autor Teste"}
    ]

    with patch("src.motivacao.requests.get", return_value=resposta_falsa):
        resultado = buscar_frase_motivacional()
        assert "Acredite em você." in resultado
        assert "Autor Teste" in resultado


def test_frase_motivacional_falha_de_rede():
    """Testa se a função retorna mensagem padrão quando a API falha."""
    with patch("src.motivacao.requests.get", side_effect=Exception("Sem internet")):
        resultado = buscar_frase_motivacional()
        assert "Foco no que importa" in resultado