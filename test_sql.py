import config # Подключает конфиг
from telebot import types # Импортируем типы из модуля, чтобы создавать кнопки
import telebot # Подключаем модуль Телеграма
import urllib.request # Подключаем модуль для скачивания файлов
import pyodbc # для взаимодействия с БД
import pandas as pd # для манипулирования данными и экспорта в виде электронных таблиц

driver = 'DRIVER={SQL Server}'
server = 'SERVER=dc-sql12-db\\db' # имя сервера
db = 'DATABASE=Inventory' # имя БД
conn_str = ';'.join([driver, server, db]) 
conn = pyodbc.connect(conn_str) # Подключение БД
"""
host = "ws"
hostname = "'" + host + "'"
script = "SELECT * FROM dbo.main WHERE hostname = " + hostname # скрипт запроса к БД

df = pd.read_sql_query(script, conn) # чтение полученых данных с занесением в переменную

writer = pd.ExcelWriter('documents\\example.xlsx') # создание файла
df.to_excel(writer, sheet_name='bar') # Добавление данных из переменной с созданием листа
writer.save() # сохранение
"""
bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=['text']) # Реакция на текст
def send_text(message):
   if message.text.lower() == '90514-ws404':
      host = message.text.lower()
      hostname = "'" + host + "'"
      script = "SELECT * FROM dbo.main WHERE hostname = " + hostname
      df = pd.read_sql_query(script, conn) # чтение полученых данных с занесением в переменную
      writer = pd.ExcelWriter('documents\\example.xlsx') # создание файла
      df.to_excel(writer, sheet_name='bar') # Добавление данных из переменной с созданием листа
      writer.save() # сохранение
      file = open('documents\\example.xlsx', 'rb')
      bot.send_document(message.chat.id, file)

"""
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
"""
if __name__ == '__main__': # постоянный опрос бота
    bot.polling(none_stop=True)