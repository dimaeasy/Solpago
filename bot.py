import telebot
from payments import create_invoice
from config import TELEGRAM_TOKEN, WELCOME_MESSAGE

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, WELCOME_MESSAGE)

@bot.message_handler(commands=['pay'])
def handle_pay(message):
    invoice_url = create_invoice(user_id=message.from_user.id)
    bot.send_message(message.chat.id, f"👉 Оплатите по ссылке: {invoice_url}")

if __name__ == "__main__":
    bot.polling()
