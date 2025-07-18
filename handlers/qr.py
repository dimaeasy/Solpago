from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
import qrcode
from io import BytesIO

router = Router()

def generate_qr_code(data: str) -> BytesIO:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    output = BytesIO()
    img.save(output, format="PNG")
    output.seek(0)
    return output

@router.message(Command("qr"))
async def send_qr(message: Message):
    data = "https://solpago.com"
    qr_image = generate_qr_code(data)

    path = "qr_temp.png"
    with open(path, "wb") as f:
        f.write(qr_image.read())

    await message.answer_photo(FSInputFile(path), caption="Вот твой QR-код!")
