import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import start
from utils.logger import logger

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()

# Регистрируем хендлеры
dp.include_router(start.router)

async def main():
    logger.info("Запуск бота...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
