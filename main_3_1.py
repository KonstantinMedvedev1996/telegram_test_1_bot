import telebot
from telebot import types
from Config import Config


bot = telebot.TeleBot(Config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Go to site')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Delete photo')
    btn3 = types.InlineKeyboardButton('Change text')
    markup.row(btn2, btn3)
    file = open('./photo.png', 'rb')
    bot.send_photo(message.chat.id,file, reply_markup=markup)
    # bot.send_message(message.chat.id,'Hello !', reply_markup = markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Go to site':
        bot.send_message(message.chat.id, 'Website is open')
    elif message.text == 'Delete photo':
        bot.send_message(message.chat.id, 'Deleted')

# @bot.message_handler(content_types=['photo'])
# def get_photo(message):
#     bot.reply_to(message,'What a beautiful photo')

# @bot.message_handler(content_types=['photo'])
# def get_photo(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('Go to site', url='https://www.google.com/'))
#     bot.reply_to(message,'What a beautiful photo', reply_markup = markup)

# @bot.message_handler(content_types=['photo'])
# def get_photo(message):
#     markup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton('Go to site', url='https://www.google.com/')
#     markup.row(btn1)
#     btn2 = types.InlineKeyboardButton('Delete photo', callback_data='delete')
#     btn3 = types.InlineKeyboardButton('Change text', callback_data='edit')
#     markup.row(btn2, btn3)
#     bot.reply_to(message,'What a beautiful photo', reply_markup = markup)

# @bot.callback_query_handler(func=lambda callback: True)
# def callback_message(callback):
#     if callback.data == 'delete':
#         bot.delete_message(callback.message.chat.id, callback.message.message_id - 1 )
#     elif  callback.data == 'edit':
#         bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)   

bot.polling(none_stop=True)