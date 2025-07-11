import requests

API_URL = "https://voidsearch.localto.net/api/search"
API_KEY = "WM3t-Av5u-thfP-GiBV-sM3B"

def buscar_dados(base, valor):
    try:
        params = {
            "Access-Key": API_KEY,
            "Base": base,
            "Query": valor
        }
        response = requests.get(API_URL, params=params, timeout=10)
        try:
            data = response.json()
        except ValueError:
            return "Erro: resposta da API não está em formato JSON válido."

        if isinstance(data, dict):
            if not data:
                return "Nenhum dado encontrado para a consulta."
            texto = ""
            for chave, valor in data.items():
                texto += f"🔹 {chave}: {valor}\n"
            return texto.strip()
        else:
            return "Erro: formato de dados inesperado na resposta da API."
    except requests.exceptions.RequestException as e:
        return f"Erro na requisição: {e}"
    except Exception as e:
        return f"Erro inesperado: {e}"
