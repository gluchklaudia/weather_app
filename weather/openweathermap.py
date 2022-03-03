import os

class OpenWeatherMap:
    api_url = "http://api.openweathermap.org"

    def __init__(self, api_key: str=None):
        self.api_key = api_key if api_key else os.environ["api_key"]