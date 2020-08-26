import config
import telebot
from telebot import apihelper
import urllib.request 
import pyodbc # для взаимодействия с БД
import pandas as pd # для манипулирования данными и экспорта в виде электронных таблиц

driver = 'DRIVER={SQL Server}'
server = 'SERVER=dc-sql12-db\\db' # имя сервера
db = 'DATABASE=Inventory' # имя БД
conn_str = ';'.join([driver, server, db]) 
conn = pyodbc.connect(conn_str) # Подключение БД

script = """
SELECT * FROM dbo.main WHERE hostname = '90514-ws404'
""" # скрипт запроса к БД

df = pd.read_sql_query(script, conn) # чтение полученых данных с занесением в переменную

writer = pd.ExcelWriter('documents\\example.xlsx') # создание файла
df.to_excel(writer, sheet_name='bar') # Добавление данных из переменной с созданием листа
writer.save() # сохранение

bot_kz = telebot.TeleBot(config.token)
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Привет', 'Пока')
keyboard1.row('пошел', 'на')

@bot_kz.message_handler(commands=['start']) # Реакция на команду /
def start_message(message):
    bot_kz.send_message(message.chat.id, 'Привет, надеюсь ты найдешь здесь чтонибудь полезное,' + message.from_user.first_name + ', или иди нахуй!', reply_markup=keyboard1)

@bot_kz.message_handler(commands=['help'])  # Реакция на команду /
def help_command(message):  
    keyboard = telebot.types.InlineKeyboardMarkup()  
    keyboard.add(telebot.types.InlineKeyboardButton('Не пиши мне', url='https://telegram.me/LorD_222'))
    bot_kz.send_message(message.chat.id,'Да-да я создал', reply_markup=keyboard)

@bot_kz.message_handler(content_types=['text']) # Реакция на текст
def send_text(message):
   if message.text.lower() == 'привет':
        bot_kz.send_message(message.chat.id, 'Привет, ' + message.from_user.first_name)
   elif message.text.lower() == 'пока':
        bot_kz.send_message(message.chat.id, 'Прощай, ' + message.from_user.first_name)
   elif message.text.lower() == 'lol':
        bot_kz.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIB2V87sIDn8yqd9p3Davc-VXwIeFy7AAJGAAPb234AAVm5HRXjKXZ3GgQ')
   elif message.text.lower() == 'photo':
        file = open('documents\\Photo.png', 'rb')
        bot_kz.send_photo(message.chat.id, file)
   elif message.text.lower() == 'document':
        file = open('documents\\file_10.xlsx', 'rb')
        bot_kz.send_document(message.chat.id, file)


@bot_kz.message_handler(content_types=["document"]) # Документ
def handle_docs_audio(message):
    # Получим ID Стикера
    document_id = message.document.file_id
    # Нужно получить путь, где лежит файл на Сервере Телеграмма
    file_info = bot_kz.get_file(document_id)
    # Теперь формируем ссылку и скачивам файл
    urllib.request.urlretrieve(f'http://api.telegram.org/file/bot{config.token}/{file_info.file_path}', file_info.file_path)

@bot_kz.message_handler(content_types=["sticker"]) # Скачать стикер
def handle_docs_audio(message):
    # Получим ID Стикера
    sticker_id = message.sticker.file_id
    # Нужно получить путь, где лежит файл стикера на Сервере Телеграмма
    file_info = bot_kz.get_file(sticker_id)
    # Теперь формируем ссылку и скачивам файл
    urllib.request.urlretrieve(f'http://api.telegram.org/file/bot{config.token}/{file_info.file_path}', file_info.file_path)

if __name__ == '__main__':
    bot_kz.polling(none_stop=True)


