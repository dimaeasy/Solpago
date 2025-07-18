import qrcode
from io import BytesIO

def generate_qr_code(data: str) -> BytesIO:
    """Генерирует QR-код и возвращает его как изображение в памяти (BytesIO)."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img_byte_array = BytesIO()
    img.save(img_byte_array, format='PNG')
    img_byte_array.seek(0)
    return img_byte_array
