import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('OPENWEATHER_API_KEY')
CITY_ID = '524901'  # Example: Moscow
URL = f'http://api.openweathermap.org/data/2.5/forecast?id={CITY_ID}&appid={API_KEY}&units=metric'

def get_weather_forecast():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        for item in data['list'][:5]:  # Display first 5 forecast entries
            dt_txt = item['dt_txt']
            temp = item['main']['temp']
            description = item['weather'][0]['description']
            print(f"{dt_txt}: {temp}°C, {description}")
    else:
        print("Failed to fetch data:", response.status_code)

if __name__ == "__main__":
    get_weather_forecast()
