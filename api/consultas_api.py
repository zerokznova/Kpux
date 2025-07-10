import requests

API_KEY = "WM3t-Av5u-thfP-GiBV-sM3B"
URL = "https://voidsearch.localto.net/api/search"

def consultar_api(base, info):
    try:
        response = requests.get(URL, params={
            "Access-Key": API_KEY,
            "Base": base,
            "Info": info
        }, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if not data:
                return "⚠️ Nenhuma informação encontrada."
            resultado = ""
            for item in data:
                for k, v in item.items():
                    resultado += f"{k.upper()}: {v}\n"
                resultado += "\n"
            return resultado.strip()
        return f"Erro {response.status_code}: {response.text}"
    except Exception as e:
        return f"Erro: {str(e)}"
