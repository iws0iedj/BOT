import os
import telebot
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands="Hello")
def welcom(message):
    bot.reply_to(message , "WElcom in my bot")

bot.polling()