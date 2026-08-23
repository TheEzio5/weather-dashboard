
from weather_api import WeatherAPI

api = WeatherAPI()
city = input("Enter city: ")
weather = api.get_weather(city)

if weather:
    print(f'City name: {weather["name"]}')
    print(f'{weather["main"]["temp"]} °C')
    print(f'Description: {weather["weather"][0]["description"]}')


# print(api.api_key)
