import os
import urllib
import requests
from dataclasses import dataclass


@dataclass
class Coordinates:
    lat: float
    lon: float


class OpenWeatherMap:
    _api_url = "http://api.openweathermap.org"
    _geocoding_endpoint_template = "geo/1.0/direct?q={city_name}&limit=1&appid={api_key}"
    
    def __init__(self, api_key: str = None):
        # os.environ - wczytywanie zmiennych systemowych.
        self.api_key = api_key if api_key else os.environ["api_key"]

    def get_city_coordinates(self, city_name: str):
        endpoint = self._geocoding_endpoint_template.format(
            api_key=self.api_key, city_name=city_name
        )
        url = urllib.parse.urljoin(self._api_url, endpoint)
        response = requests.get(url)
        if response.ok:
            first_data = response.json()[0]
            return Coordinates(lat=first_data["lat"], lon=first_data["lon"])
        else:
            print(response.status_code)