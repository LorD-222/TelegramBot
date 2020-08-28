import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token, threaded=True)

@bot.message_handler(commands=["start"])
def location(message):
   bot.send_location(message.chat.id, latitude = '59.883431', longitude = '30.248957' )



bot.polling()