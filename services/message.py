from services.api import get_weather



async def get_text_from_weather(text) -> str:
    weather = await get_weather(text)
    return f"Погорода в городе: {weather.city}\nТемпература: {weather.temp}C°, ощущается как: {weather.temp_feels}C° {weather.smile}\nВетер: {weather.wind_speed} м/c \nВосход: {weather.sunrise_timestamp}\nЗакат: {weather.sunset_timestamp}."