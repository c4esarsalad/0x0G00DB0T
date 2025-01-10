import random
import os
import telebot
from bot_token import token

bot = telebot.TeleBot(token)

def send_meme(message):
    img_name = random.choice(os.listdir("images"))
    with open(f'images/{img_name}', 'rb') as f:
        bot.send_photo(message.chat.id, f)
