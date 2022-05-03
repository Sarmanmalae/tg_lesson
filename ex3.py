import datetime
import logging
import time
from random import randint

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = ''

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def process_start_command(message: types.Message):
    await message.reply("Привет! Напиши мне что-нибудь!")


@dp.message_handler(commands=['time'])
async def time_(message: types.Message):
    a = datetime.datetime.now()
    await message.reply(f'{a.hour}:{a.minute}')


@dp.message_handler(commands=['date'])
async def date(message: types.Message):
    a = datetime.datetime.now()
    await message.reply(f'{a.day}.{a.month}.{a.year}')


@dp.message_handler(commands=['set_timer'])
async def set_timer(message: types.Message):
    t = message.get_args()
    time.sleep(int(t))
    await message.reply('a')


@dp.message_handler()
async def echo_bot(message: types.Message):
    await message.reply(f'Я получил сообщение "{message.text}"')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
