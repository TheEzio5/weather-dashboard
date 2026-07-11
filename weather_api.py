import os
import requests
from dotenv import load_dotenv

class WeatherAPI:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("API_KEY")

    def get_weather(self, city):
        city = city.lower()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        print(response.status_code)
        weather = response.json()

        print(f'City name: {weather["name"]}')
        print(f'{weather["main"]["temp"]} °C')
        print(f'Description: {weather["weather"][0]["description"]}')