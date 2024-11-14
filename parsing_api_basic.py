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
city = input("Введите название города (ENG/РУС): ")
fields = "categories,name,rating,location"
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
    
# Компановка данных

    data = json.loads(response.text)

# Формирование запроса пользователю на выбор категории

    venues = data["results"]
    categories = set(venue["categories"][0]["name"] for venue in venues)
    print(f"В городе {city} есть:")
    print()
    print(*categories, sep='\n')
    print()
    user_choise = input("Введите название категории для поиска: ").title()
    print()
# Вывод ответ пользователю
    print(f'В выбранной категории {user_choise} найдено:')
    print()
    for venue in venues:
        if venue["categories"][0]["name"] == user_choise:
            print("Название:", venue["name"])
            print("Рейтинг:", venue["rating"])
            print("Адрес:", venue["location"]["formatted_address"])
            print()
    

else:
    print("Запрос API завершился неудачей с кодом состояния:", response.status_code)
    print(response.text)
