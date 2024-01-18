import telebot

bot = telebot.TeleBot('6731981200:AAFi95AM78FH6oEqY-tK7Qpge7B99ecF08o')

@bot.message_handler(commands=['start'])
def main(message):
    bot.sed_message(message.chat.id, 'Hello, World!')

bot.polling(non_stop=True)