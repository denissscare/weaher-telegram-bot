from aiogram import Dispatcher, Bot, types
from config import BOT_TOKEN 
from services.message import get_text_from_weather 
import asyncio

dispatcher = Dispatcher()

@dispatcher.message()
async def weather(message: types.Message):
    await message.answer(text=await get_text_from_weather(message.text))


async def main():
    bot = Bot(token=BOT_TOKEN)
    await dispatcher.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())