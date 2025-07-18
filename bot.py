from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InputFile
from config import BOT_TOKEN
from qr import generate_qr_code
import os

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer("Привет! Отправь команду /qr чтобы получить QR-код.")

@dp.message_handler(commands=["qr"])
async def qr_handler(message: types.Message):
    data = "https://solpago.com"
    path = "qr.png"
    with open(path, "wb") as f:
        f.write(generate_qr_code(data).read())
    await message.answer_photo(InputFile(path), caption="Твой QR-код")
    os.remove(path)

if __name__ == "__main__":
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
