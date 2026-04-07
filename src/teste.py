import requests

url = "http://127.0.0.1:5000/leituras"

dados = {
    "temperatura": 25,
    "umidade": 60
}

response = requests.post(url, json=dados)

print(response.json())