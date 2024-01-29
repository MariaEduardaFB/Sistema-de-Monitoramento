import requests
from APIrequest import API_KEY

def obter_imagens_satelites(latitude, longitude):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    parametros = {
        'lat': latitude,
        'lon': longitude,
        'appid': API_KEY
    }

    resposta = requests.get(base_url, params=parametros)

    # Verificar se a solicitação foi bem-sucedida (código de status HTTP 200)
    if resposta.status_code == 200:
        # Salvar a resposta, que contém dados meteorológicos, em um arquivo JSON ou processar conforme necessário
        with open('dados_meteorologicos.json', 'w') as f:
            f.write(resposta.text)
    else:
        print(f"Erro na solicitação: {resposta.status_code}")

# Substitua 'SUA_CHAVE_API' pela chave da sua conta no OpenWeatherMap
latitude = -15.0
longitude = -45.0

obter_imagens_satelites(latitude, longitude)
