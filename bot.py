import telebot

import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! я говно.")

@bot.message_handler(commands=['bye'])
def bye_message(message):
    bot.send_message(message.chat.id, "Давай братишка.")


import random
@bot.message_handler(commands=['coin'])
def coin_meassage(message):
    result = random.choice(["Орёл🦅", "Решка🟡"])
    bot.send_message(message.chat.id, f"Монетка подброшена: {result}")


bot.infinity_polling()
