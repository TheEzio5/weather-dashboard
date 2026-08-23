
from weather_api import WeatherAPI

api = WeatherAPI()
city = input("Enter city: ")
weather = api.get_weather(city)

if weather:
    print(f'City name: {weather["name"]}')
    print(f'{weather["main"]["temp"]} °C')
    print(f'Feels like: {weather["main"]["feels_like"]} °C')
    print(f'Min temperature: {weather["main"]["temp_min"]} °C')
    print(f'Max temperature: {weather["main"]["temp_max"]} °C')
    print(f'Humidity: {weather["main"]["humidity"]}%')
    print(f'Wind speed: {weather["wind"]["speed"]} m/s')
    print(f'Description: {weather["weather"][0]["description"]}')




# print(api.api_key)
