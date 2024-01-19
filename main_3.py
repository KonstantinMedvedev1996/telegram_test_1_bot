import telebot
from telebot import types

bot = telebot.TeleBot('6731981200:AAFi95AM78FH6oEqY-tK7Qpge7B99ecF08o')


# @bot.message_handler(content_types=['photo'])
# def get_photo(message):
#     bot.reply_to(message,'What a beautiful photo')

# @bot.message_handler(content_types=['photo'])
# def get_photo(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('Go to site', url='https://www.google.com/'))
#     bot.reply_to(message,'What a beautiful photo', reply_markup = markup)

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Go to site', url='https://www.google.com/')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Delete photo', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Change text', callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message,'What a beautiful photo', reply_markup = markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1 )
    elif  callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)   

bot.polling(none_stop=True)