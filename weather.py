import datetime 
from translate import Translator
import requests

from utiles import wind_string, wind_direction

def get_today_weather() -> str:

    url = 'http://api.openweathermap.org/data/2.5/weather?q=moscow&appid=b96c6038f2b65948ecc7733eb3336864&units=metric'

    answer = requests.get(url)

    weather_json = answer.json()

    today = datetime.datetime.today().strftime("%m/%d/%Y, %H:%M")

    translator = Translator(from_lang="english",to_lang="russian")

    result = f'Weather ☁️ - {today}\n\n'
    result += f'Погода в Москве: {translator.translate(weather_json["weather"][0]["main"])}\n'
    result += f'{translator.translate(weather_json["weather"][0]["description"])}, температура: {weather_json["main"]["temp_min"]} - {weather_json["main"]["temp_max"]}°C\n'
    result += f'Давление: {weather_json["main"]["pressure"]} мм рт. ст., влажность: {weather_json["main"]["humidity"]}%\n'
    result += f'Ветер: {wind_string(float(weather_json["wind"]["speed"]))}, {float(weather_json["wind"]["speed"])} м/с, {wind_direction(float(weather_json["wind"]["deg"]))}'

    return result