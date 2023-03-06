import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

API_TOKEN = '5517340699:AAF3pLYBW3wlELO1k8fC1WghoEa6BP1daPA'

logging.basicConfig(level=logging.INFO)

bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot)

button1 = KeyboardButton("Hello")
button2 = KeyboardButton("Telegram")
button3 = KeyboardButton("Telegram Kanalimiz")
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1).add(button2).add(button3)


@dp.message_handler(commands=["start", "help"])
async def welcome(message: types.Message):
    await message.reply("Hello! in Guntzer", reply_markup=keyboard1)

@dp.message_handler()
async def kb_answer(message: types.Message):
    if message.text == "Saloom":
        await message.answer(" Salom havayu karoche")
    elif message.text == "Telegram":
        await message.answer("https://t.me/Bepuldarslar_uzbbot")
    elif message.text == "Telegram Kanalimiz":
        await message.answer("https://t.me/Bepul_darslar_uzb")
    else:
        await message.answer(f"Yuor  message is: {message.text}")
    



@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer("Hi there! I'm an AIogram bot, how can I help you today?")

@dp.message_handler(commands="sayhi")
async def sayhi(message: types.Message):
    await message.answer("Hello World")


@dp.message_handler(content_types=types.ContentType.ANY)
async def echo_message(message: types.Message):
    if message.text == "salom" or message.text == "Salom":
        await message.answer("Salom yaxshimisiz")
    elif message.text == "Qalesan" or message.text == "qalesan":
        await message.answer("Yaxshi o'zizchi")
    elif message.text == "yordam ber":
        await message.answer("Nma yordam kerak")
    elif message.text == "hazillashdim":
        await message.answer("Yaxshi")
    elif message.text == "Seni isming nma" or message.text == "seni isming nma" or message.text == "sani isming nma":
        await message.answer("Bot")
    elif message.text == "Men kimman":
        await message.answer("Bilmadim")
    else:
        await bot.send_message(chat_id=message.from_user.id, text=message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)