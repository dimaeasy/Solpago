from aiogram import Router
from aiogram.types import Message, BufferedInputFile
from aiogram.filters import Command
from utils.qr import generate_qr_code

router = Router()

@router.message(Command("qr"))
async def cmd_qr(message: Message):
    data = message.text.removeprefix("/qr").strip()
    if not data:
        data = "https://solpago.com"

    image_bytes = generate_qr_code(data)
    qr_file = BufferedInputFile(image_bytes.read(), filename="qrcode.png")
    
    await message.answer_photo(qr_file, caption=f"QR для:\n<code>{data}</code>")
