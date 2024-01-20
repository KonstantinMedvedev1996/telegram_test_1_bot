import telebot
from Config import Config

bot = telebot.TeleBot(Config.TOKEN)

@bot.message_handler(commands=['start'])
def main(message):
    bot.sed_message(message.chat.id, 'Hello, World!')

bot.polling(non_stop=True)