import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def send_welcome(message: types.Message):
    data = message.text
    summa = sum([1 for char in data if char.lower() in ['a', 'e', 'i', 'o', 'u']])
    if summa > 5:
        await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
