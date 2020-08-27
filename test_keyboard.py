import config
# Подключаем модуль случайных чисел 
import random
# Подключаем модуль для Телеграма
import telebot
# Указываем токен
bot = telebot.TeleBot(config.token)
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types

@bot.message_handler(commands=["start"])
def inline(message):
  key = types.InlineKeyboardMarkup()
  but_1 = types.InlineKeyboardButton(text="NumberOne", callback_data="NumberOne")
  but_2 = types.InlineKeyboardButton(text="NumberTwo", callback_data="NumberTwo")
  but_3 = types.InlineKeyboardButton(text="NumberTree", callback_data="NumberTree")
  key.add(but_1, but_2, but_3)
  bot.send_message(message.chat.id, "ВЫБЕРИТЕ КНОПКУ", reply_markup=key)

@bot.callback_query_handler(func=lambda c:True)
def inline(c):
   if c.data == 'NumberOne':
      bot.send_message(c.message.chat.id, 'Это кнопка 1')
   if c.data == 'NumberTwo':
      bot.send_message(c.message.chat.id, 'Это кнопка 2')
   if c.data == 'NumberTree':
      key = types.InlineKeyboardMarkup()
      but_4 = types.InlineKeyboardButton(text="Number4", callback_data="Number4")
      but_5 = types.InlineKeyboardButton(text="Number5", callback_data="Number5")
      but_6 = types.InlineKeyboardButton(text="Number6", callback_data="Number6")
      key.add(but_4, but_5, but_6)
      bot.send_message(c.message.chat.id, 'Это кнопка 3', reply_markup=key)
   if c.data == 'Number4':
      key = types.InlineKeyboardMarkup()
      but_7 = types.InlineKeyboardButton(text="Number7", callback_data="Number7")
      but_8 = types.InlineKeyboardButton(text="Number8", callback_data="Number8")
      but_9 = types.InlineKeyboardButton(text="Number9", callback_data="Number9")
      key.add(but_7, but_8, but_9)
      bot.send_message(c.message.chat.id, 'Это кнопка 4', reply_markup=key)


if __name__ == '__main__': # постоянный опрос бота
    bot.polling(none_stop=True)