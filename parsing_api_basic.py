'''
Сценарий Foursquare
Напишите сценарий на языке Python, который предложит пользователю ввести интересующую его категорию (например, кофейни, музеи, парки и т.д.).
Используйте API Foursquare для поиска заведений в указанной категории.
Получите название заведения, его адрес и рейтинг для каждого из них.
Скрипт должен вывести название и адрес и рейтинг каждого заведения в консоль.'''

import requests
import json
from pprint import pprint

# Конечная точка API
endpoint = "https://api.foursquare.com/v3/places/search"

# Определение параметров для запроса API
city = 'Ufa' #input("Введите название города (ENG/РУС): ")
fields = "name,rating,location"
params = {"near": city,
          "fields": fields}

headers = {
    "Accept": "application/json",
    "Authorization": "fsq3iqqZ4EkGp4yrlY3xU3Hmqsd+yNyeXFGabhLAxNo2+l4="
}

# Отправка запроса API и получение ответа
response = requests.get(endpoint, params=params, headers=headers)

# Проверка успешности запроса API
if response.status_code == 200:
    print("Успешный запрос API!")

# Компановка вывода

    data = json.loads(response.text)
    # venues = data["results"]
    # categories = [venue["categories"][0]["name"] for venue in venues]

    # for category in categories:
    #     print(category)
    # for venue in venues:
    #     print("Название:", venue["name"])
    #     print("Адрес:", venue["location"]["address"])
    #     print("\n")
    # for venue in venues: 
    #     pprint(venue['categories'][0]['name'])

else:
    print("Запрос API завершился неудачей с кодом состояния:", response.status_code)
    print(response.text)

pprint(data)