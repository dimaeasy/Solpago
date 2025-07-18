from aiogram import Router, types
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer("Добро пожаловать в Solpago! 🧾\n\nОтправь сумму, которую хочешь оплатить.")
