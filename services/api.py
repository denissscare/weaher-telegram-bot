import datetime
import aiohttp
from config import WEATHER_TOKEN
from utils import smile_code
import json
from dataclasses import dataclass

@dataclass(slots=True, frozen=True)
class WeatherParams:
    city: str
    temp: float
    temp_feels: float
    description: str
    wind_speed: float
    sunrise_timestamp: datetime
    sunset_timestamp: datetime
    smile: str



async def get_weather(city) -> WeatherParams:
    data = await _openweather_resp(city)
    weather = _parse_data(data)
    return weather


async def _openweather_resp(city: str) -> str:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_TOKEN}&units=metric"
    async with aiohttp.ClientSession() as session: 
        async with session.get(url) as resp:
            response_data = await resp.text()
            return response_data

def _parse_data(resp: str) -> WeatherParams:
    data = json.loads(resp)

    if data["weather"][0]["main"] in smile_code:
        smile = smile_code[data["weather"][0]["main"]]
    else:
        smile = ""

    return WeatherParams(
        city=data['name'],
        temp=data['main']['temp'],
        temp_feels=data['main']['feels_like'],
        description=data["weather"][0]["main"],
        wind_speed=data["wind"]["speed"],
        sunrise_timestamp=datetime.datetime.fromtimestamp(data["sys"]["sunrise"]),
        sunset_timestamp=datetime.datetime.fromtimestamp(data["sys"]["sunset"]),
        smile=smile
    )