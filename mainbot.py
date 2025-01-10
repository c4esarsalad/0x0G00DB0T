import telebot
from telebot import types

from bot_password import gen_pass
from bot_coin_game import gen_emodji, flip_coin
from bot_send_meme import send_meme
from bot_ducks_meme import duck
from bot_token import token

bot = telebot.TeleBot(token)

def send_menu(chat_id):

    markup = types.InlineKeyboardMarkup()
    
    button1 = types.InlineKeyboardButton("Сгенерировать пароль", callback_data='generate_password')
    button2 = types.InlineKeyboardButton("Сыграть в орла и решку", callback_data='flip_coin')
    button3 = types.InlineKeyboardButton("Рандомный эмодзи", callback_data='random_emoji')
    button4 = types.InlineKeyboardButton("Рандомный мем", callback_data='random_meme')
    button5 = types.InlineKeyboardButton("Утки", callback_data='duck')
    
    markup.add(button1, button2)
    markup.add(button3, button4)
    markup.add(button5)
    
    bot.send_message(chat_id, "Выберите действие:", reply_markup=markup)

@bot.message_handler(commands=['start'])
def start(message):
    send_menu(message.chat.id)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'generate_password':
        password = gen_pass(10)
        bot.send_message(call.message.chat.id, f"Вот твой пароль: {password}")
    elif call.data == 'flip_coin':
        result = flip_coin()
        bot.send_message(call.message.chat.id, f"Результат: {result}")
    elif call.data == 'random_emoji':
        emoji = gen_emodji()
        bot.send_message(call.message.chat.id, f"Эмодзи: {emoji}")
    elif call.data == 'random_meme':
        send_meme(call.message)
    elif call.data == 'duck':
        duck(bot, call.message.chat.id)
    
    send_menu(call.message.chat.id)

print("Бот запущен!")

bot.polling()
