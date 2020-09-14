import config
import telebot
from telebot import types
import subprocess

bot = telebot.TeleBot(config.token, threaded=True)

@bot.message_handler(content_types=['text']) # Реакция на текст
def send_text(message):
   text = message.text.lower()
   pars = text.rsplit()
   iff = pars[0]
   WS = pars[1]
   if iff.lower() == "пинг":
      args = ["ping", WS]
      process = subprocess.Popen(args, stdout=subprocess.PIPE)
      data = process.communicate()
      bot.send_message(message.chat.id, data)


bot.polling()