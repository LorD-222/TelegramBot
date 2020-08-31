import config
import telebot
from telebot import apihelper
from telebot import types
import datetime
import os


 
### Token telegram bot
bot = telebot.TeleBot(config.token, threaded=True)
 
### Функция проверки авторизации
def autor(chatid):
    strid = str(chatid)
    for item in config.users:
        if item == strid:
            return True
    return False

### Клавиатура
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('document','/start')

@bot.message_handler(commands=['start'])
def start_message(message):
   if autor(message.chat.id):
      cid = message.chat.id
      message_text = message.text
      user_id = message.from_user.id
      user_name = message.from_user.first_name
      bot.send_message(message.chat.id, 'Привет, ' + user_name + ' Что ты хочешь от меня, собака сутулая!', reply_markup=keyboard1)
      bot.send_sticker(message.chat.id, 'CAADAgAD6CQAAp7OCwABx40TskPHi3MWBA')
   else:
      bot.send_message(message.chat.id, 'Тебе сюда нельзя. Твой ID: ' + str(message.chat.id))
      bot.send_sticker(message.chat.id, 'CAADAgADcQMAAkmH9Av0tmQ7QhjxLRYE')

@bot.message_handler(content_types=['text']) # Реакция на текст
def send_text(message):
   if autor(message.chat.id): # проверка прользователя
      if message.text.lower() == 'document':
         file = open('documents\\file_10.xlsx', 'rb')
         bot.send_document(message.chat.id, file)
   else:
        bot.send_message(message.chat.id, 'Тебе сюда нельзя. Твой ID: ' + str(message.chat.id))
        bot.send_sticker(message.chat.id, 'CAADAgADcQMAAkmH9Av0tmQ7QhjxLRYE')

if __name__ == '__main__': # постоянный опрос бота
    bot.polling(none_stop=True)