import config # Подключает конфиг
from telebot import types # Импортируем типы из модуля, чтобы создавать кнопки
import telebot # Подключаем модуль Телеграма
import urllib.request # Подключаем модуль для скачивания файлов
import pyodbc # для взаимодействия с БД
import pandas as pd # для манипулирования данными и экспорта в виде электронных таблиц
import re
import io
### Token telegram bot
bot = telebot.TeleBot(config.token, threaded=True)

@bot.message_handler(content_types=['text'])  # Добавление юзеров
def help_command(message):
   text = message.text.lower()
   pars = text.rsplit()
   iff = pars[0]
   id_user = pars[1]
   if iff.lower() == "добавь":
      f = open("config.py", "r+")
      lines = f.read()
      id_users = lines
      index = len(id_users)
      f.seek(index)
      f.write(f"', '{id_user}']")
      f.close()
      data = config.users
      bot.send_message(message.chat.id, 'Добавлен')

if __name__ == '__main__': # постоянный опрос бота
    bot.polling(none_stop=True)
