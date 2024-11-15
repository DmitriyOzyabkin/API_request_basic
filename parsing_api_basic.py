'''
Сценарий Foursquare
Напишите сценарий на языке Python, который предложит пользователю ввести интересующую его категорию (например, кофейни, музеи, парки и т.д.).
Используйте API Foursquare для поиска заведений в указанной категории.
Получите название заведения, его адрес и рейтинг для каждого из них.
Скрипт должен вывести название и адрес и рейтинг каждого заведения в консоль.'''

import requests
import json

# Конечная точка API
endpoint = "https://api.foursquare.com/v3/places/search"

# Определение параметров для запроса API
city = input("Введите название города (ENG/РУС): ")
fields = "categories,name,rating,location"
params = {"near": city,
          "fields": fields,
          "limit": 50}

headers = {
    "Accept": "application/json",
    "Authorization": "fsq3W/r0QxmECG3mWEQIjFHnPrZ14YRDtn6AJsPryv6pBZM="
}

# Отправка запроса API и получение ответа
response = requests.get(endpoint, params=params, headers=headers)

# Проверка успешности запроса API
if response.status_code == 200:
    
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

# Вывод ответа пользователю
    print(f'В выбранной категории {user_choise} найдено:')
    print()
    for venue in venues:
        if venue["categories"][0]["name"] == user_choise:
            print("Название:", venue["name"])
            print("Рейтинг:", venue["rating"])
            print("Адрес:", venue["location"]["formatted_address"])
            print()
    
# Вывод ошибки
else:
    print("Запрос API завершился неудачей с кодом состояния:", response.status_code)
    print(response.text)
