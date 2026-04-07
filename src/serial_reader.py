import requests
import random
import time

URL = 'http://localhost:5000/leituras'

while True:
    dados = {
        "temperatura": round(random.uniform(20, 30), 2),
        "umidade": round(random.uniform(40, 80), 2)
    }

    requests.post(URL, json=dados)
    print("Enviado:", dados)

    time.sleep(5)