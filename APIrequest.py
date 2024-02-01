import requests

API_KEY = '5b21421170493bdae3c5059f07a9add7'

city ='Iguatu'

link = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=pt_br'

requisicao = requests.get(link)
requisicao_dic = requisicao.json()
descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp'] - 273.15
print(city)
print(descricao)
print(f'{temperatura}°C')
