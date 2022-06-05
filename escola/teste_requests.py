import requests

# GET avaliações

avaliacoes = requests.get("http://localhost:8000/api/v2/avaliacoes/")

print(avaliacoes.json())
