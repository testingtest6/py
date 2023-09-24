from random import randint
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton,ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove
import json



bot =Bot(token='6347482601:AAFQcvJ8gDrauzlTpcP0BEKe4QF2p4YMEaI')

dp=Dispatcher(bot)

keyboard = InlineKeyboardMarkup()
button = InlineKeyboardButton('text', url='http://flappyg.topg-ai.org/')
keyboard.add(button)

@dp.callback_query_handler()
async def choosed(call :types.CallbackQuery):
    await call.answer(url="https://flappyg.topg-ai.org/")

   


executor.start_polling(dp)

