from weather.openweathermap import OpenWeatherMap, Coordinates
from unittest import mock
import unittest
import requests_mock


def test_get_city_coordinates_ok_scenario():
    open_weather_map = OpenWeatherMap(api_key="fake_key")
    with requests_mock.Mocker() as m:
        m.get(
            "http://api.openweathermap.org/geo/1.0/direct?q=London",
            status_code=200,
            json=[
                {
                    "lat": 51.5073219,
                    "lon": -0.1276474,
                    "city": "London",
                }
            ],
        )
        assert open_weather_map.get_city_coordinates("London") == Coordinates(
            lat=51.5073219,
            lon=-0.1276474,
        )


def test_get_city_coordinates_when_during_connection_error_occur():
    open_weather_map = OpenWeatherMap(api_key="fake_key")
    with requests_mock.Mocker() as m:
        m.get("http://api.openweathermap.org/geo/1.0/direct?q=London", status_code=404)
        assert open_weather_map.get_city_coordinates("London") == None
