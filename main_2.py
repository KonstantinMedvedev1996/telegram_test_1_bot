import telebot
import webbrowser

bot = telebot.TeleBot('6731981200:AAFi95AM78FH6oEqY-tK7Qpge7B99ecF08o')

@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://www.google.com')

@bot.message_handler(commands=['start', 'main'])
def main(message):
    bot.send_message(message.chat.id, 'Hello, World!')
    
@bot.message_handler(commands=['hello'])
def main(message):
    bot.send_message(message.chat.id, f'Hello , {message.from_user.first_name} {message.from_user.last_name}')

@bot.message_handler(commands=['info'])
def main(message):
    bot.send_message(message.chat.id, message)
    
@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Hello</b> <em><u>information</u></em>!', parse_mode='HTML')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'hi':
        bot.send_message(message.chat.id, f'Hello , {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
    elif message.text.lower() == '/begin':
        bot.send_message(message.chat.id, 'yes, World!')

bot.infinity_polling()