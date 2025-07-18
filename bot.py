import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
from config import BOT_TOKEN
from handlers import start
from utils.logger import logger
from utils.qr import generate_qr_code

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()

# Регистрируем хендлеры
dp.include_router(start.router)

@dp.message(Command("qr"))
async def cmd_qr(message: Message):
    data = "https://solpago.com"  # Здесь можно вставить любой текст или ссылку
    image_path = generate_qr_code(data)
    
    file = FSInputFile(image_path, filename="qrcode.png")
    await message.answer_photo(file, caption="Вот твой QR-код!")

async def main():
    logger.info("Запуск бота...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
