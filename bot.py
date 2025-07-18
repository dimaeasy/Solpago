from aiogram import types, Dispatcher

async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот для Solpago 🧾")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start"])
