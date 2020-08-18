import config
import telebot
from telebot import apihelper
import urllib.request 

bot_kz = telebot.TeleBot(config.token)
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Привет', 'Пока')

@bot_kz.message_handler(commands=['start'])
def start_message(message):
    bot_kz.send_message(message.chat.id, 'Привет, надеюсь ты найдешь здесь чтонибудь полезное,' + message.from_user.first_name + ', или иди нахуй!', reply_markup=keyboard1)

@bot_kz.message_handler(commands=['help'])  
def help_command(message):  
    keyboard = telebot.types.InlineKeyboardMarkup()  
    keyboard.add(telebot.types.InlineKeyboardButton('Не пиши мне', url='https://telegram.me/LorD_222'))
    bot_kz.send_message(message.chat.id,'Да-да я создал', reply_markup=keyboard)

@bot_kz.message_handler(content_types=['text'])
def send_text(message):
   if message.text.lower() == 'привет':
        bot_kz.send_message(message.chat.id, 'Привет, мой создатель')
   elif message.text.lower() == 'пока':
        bot_kz.send_message(message.chat.id, 'Прощай, создатель')
   elif message.text.lower() == 'lol':
        bot_kz.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIB2V87sIDn8yqd9p3Davc-VXwIeFy7AAJGAAPb234AAVm5HRXjKXZ3GgQ')
   elif message.text == 'photo':
        file = open('Photo.png', 'rb')
        bot_kz.send_photo(message.chat.id, file)
   elif message.text == 'document':
        file = open('file.txt', 'rb')
        bot_kz.send_document(message.chat.id, file)


@bot_kz.message_handler(content_types=["document"])
def handle_docs_audio(message):
    document_id = message.document.file_id
    file_info = bot_kz.get_file(document_id)
    urllib.request.urlretrieve(f'http://api.telegram.org/file/bot{config.token}/{file_info.file_path}', file_info.file_path)


@bot_kz.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

if __name__ == '__main__':
    bot_kz.polling(none_stop=True)


