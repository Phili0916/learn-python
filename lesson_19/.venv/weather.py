import requests 
import math
import os
from dotenv import load_dotenv

from pprint import pprint



load_dotenv()

def get_current_weather():
    print('\n*** Get Current Weather Conditions ***')

    city = input('\n Please Enter a City Name: \n')

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    weather_data = requests.get(request_url).json()
    # pprint(weather_data)
    
    print(f'\nThe current weather for {weather_data["name"]} is:')
    print(f'\nThe current temperature is {round(weather_data["main"]["temp"])} degrees')
    print(f'\nIt feels like {round(weather_data["main"]["feels_like"])} degrees with {weather_data["weather"][0]["description"]}.')

if __name__ == "__main__":
    get_current_weather()