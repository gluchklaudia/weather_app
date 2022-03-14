from weather.openweathermap import OpenWeatherMap, Coordinates, WeatherInfo
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


def test_get_current_weather_when_response_is_error():
    open_weather_map = OpenWeatherMap(api_key="fake_key")
    input_coordinates = Coordinates(
        lat=51.5073219,
        lon=-0.1276474,
    )
    with requests_mock.Mocker() as m:
        m.get(
            "http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric".format(
                lat=input_coordinates.lat, lon=input_coordinates.lon
            ),
            status_code=404,
        )
        assert open_weather_map.get_current_weather(city_coordinates=input_coordinates) == None


def test_get_current_weather_when_response_is_ok():
    open_weather_map = OpenWeatherMap(api_key="fake_key")
    input_coordinates = Coordinates(
        lat=51.5073219,
        lon=-0.1276474,
    )
    expected_output = WeatherInfo(city_name='London', weather='Clouds', temperature=10.36, feels_temperature=9.31)
    with requests_mock.Mocker() as m:
        m.get(
            "http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric".format(
                lat=input_coordinates.lat, lon=input_coordinates.lon
            ),
            status_code=200,
            json={
                "name": "London",
                "weather": [{"main": "Clouds"}],
                "main": {"temp": 10.36, "feels_like": 9.31},
            },
        )
        assert (
            open_weather_map.get_current_weather(city_coordinates=input_coordinates)
            == expected_output
        )
