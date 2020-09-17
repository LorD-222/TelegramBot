import config
import telebot
from telebot import types
import subprocess

bot = telebot.TeleBot(config.token, threaded=True)

filename = '\\\\dc-data\\Departments\\Дирекция по информационным технологиям\\Управление базовых ИТ-сервисов\\Отдел обслуживания вычислительной техники\\Logons\\log.txt' 
@bot.message_handler(content_types=['text']) # Реакция на текст
def send_text(message):
   with open(filename, "r+", encoding="charmap") as fin:
      read = fin.readlines()
      spisok = []
      for line in reversed(read):
         split = line.rsplit()
         login = 'rybakov'
         if split[2].lower() == login.lower():
            if len(spisok) < 25 :
               print(split)
               spisok = spisok + split
         pass # do something
   print(spisok[0:5])
   bot.send_message(message.chat.id, f"{spisok[0:5]}\n{spisok[5:10]}")

        
   

bot.polling()