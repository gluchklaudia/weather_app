from weather.openweathermap import OpenWeatherMap

def main():
    open_weather_map = OpenWeatherMap()

    print("Hello, welcome in weather app")
    while True:
        city = input("Which one city would you like check weather for?: ")
        if city:
            city_coordinates = open_weather_map.get_city_coordinates(city)
            current_weather = open_weather_map.get_current_weather(city_coordinates)
            print(current_weather)
        else:
            print("No city was provided")
        end_or_not = input("Would you like to exit? y/n: ")
        if end_or_not.lower() == "y":
            continue
        else:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()