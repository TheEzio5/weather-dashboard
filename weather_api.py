import os
import requests
from dotenv import load_dotenv

class WeatherAPI:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("API_KEY")

