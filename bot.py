from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InputFile
import qrcode
from io import BytesIO
import logging
import os

# Вставь сюда свой токен
BOT_TOKEN = "ВАШ_ТОКЕН_ЗДЕСЬ"

# Настройка логов
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Команда /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Отправь /qr текст_или_ссылку, и я сгенерирую QR-код.")

# Команда /qr
@dp.message_handler(commands=['qr'])
async def send_qr(message: types.Message):
    data = message.get_args()
    if not data:
        data = "https://solpago.com"

    # Генерация QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Сохраняем во временный файл
    img_path = "temp_qr.png"
    img.save(img_path)

    # Отправка файла
    await bot.send_photo(message.chat.id, photo=InputFile(img_path), caption=f"QR для:\n{data}")

    # Удаляем временный файл
    os.remove(img_path)

# Запуск
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
