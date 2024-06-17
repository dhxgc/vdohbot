import telebot
bot = telebot.TeleBot('7230309509:AAE1ZBCOxy7MxoSP6nMWah4VG7oE6D1F9_c')

def send_audio_hello_message(message):
    voice_message_file = open('test1.ogg', 'rb')
    bot.send_voice(message.chat.id, voice_message_file)
    voice_message_file.close()

def send_audio_event_message(message):
    voice_message_file = open('Мероприятия.ogg', 'rb')
    bot.send_voice(message.chat.id, voice_message_file)
    voice_message_file.close()

def send_audio_about_message(message):
    voice_message_file = open('О нас.ogg', 'rb')
    bot.send_voice(message.chat.id, voice_message_file)
    voice_message_file.close()

def send_audio_same_message(message):
    voice_message_file = open('Жалоба.ogg', 'rb')
    bot.send_voice(message.chat.id, voice_message_file)
    voice_message_file.close()

def send_audio_questions_message(message):
    voice_message_file = open('Частые вопросы.ogg', 'rb')
    bot.send_voice(message.chat.id, voice_message_file)
    voice_message_file.close()








#Функция для того, чтобы узнать ID текущего чата (может быть полезно, просто вызвать ее в нужном месте)
# def send_chat_id(message):
#     __chat_id = message.chat.id
#     bot.send_message(message.chat.id, __chat_id)