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
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as error:
            print(error)
            print("Could not fetch weather data.")
            return
        weather = response.json()
        return weather

        print(f'City name: {weather["name"]}')
        print(f'{weather["main"]["temp"]} °C')
        print(f'Description: {weather["weather"][0]["description"]}')