import telebot
bot = telebot.TeleBot('7230309509:AAE1ZBCOxy7MxoSP6nMWah4VG7oE6D1F9_c')

def send_sticker(message, sticker_id):
    # Отправляем стикер
    bot.send_sticker(message.chat.id, sticker=sticker_id)