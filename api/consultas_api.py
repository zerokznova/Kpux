import requests

API_URL = "https://voidsearch.localto.net/api/search"
API_KEY = "WM3t-Av5u-thfP-GiBV-sM3B"

def buscar_dados(base, valor):
    if not valor:
        return {"error": "Informe os dados que serão consultados."}

    params = {
        "Access-Key": API_KEY,
        "Base": base,
        "query": valor  # Certifique-se que seja 'query', com q minúsculo
    }

    try:
        response = requests.get(API_URL, params=params, timeout=10)
        if response.status_code == 200:
            return response.json()
        return {"error": f"Erro na requisição: {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}
