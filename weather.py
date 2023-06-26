#Create a command-line tool that accepts a city's name and returns the current weather forecast. Leverage OpenWeatherMap API to fetch weather data and parse it using Python.

import requests
import json

def get_weather(city):

    """Gets the current weather forecast for a city.

    Args:
        city (str): The name of the city.

    Returns:
        dict: A dictionary containing the weather forecast data.
    """
    api_key="71c27368758a83d80fb04bfe198abc15"
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, api_key)
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return Exception("Error getting weather forecast for {}".format(city))
    

def main():
    "The main function begin"
    city = input("Enter the name of the city: ")
    weather=get_weather(city)
    print("The current weather in {} is {} degree Fahrenheit, {} degree Celsius with {} and {}% humidity." .format(city, weather["main"]["temp"], weather["main"]["temp_min"], weather["weather"][0]["description"],weather["main"]["humidity"]))

if __name__ == "__main__":
    main() 