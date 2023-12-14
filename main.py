import telebot
from telebot import types
import random

bot = telebot.TeleBot("TOKEN??????")

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Рандомное число"), types.KeyboardButton("Рандомный напиток"), types.KeyboardButton("Рандомный стикер"))
    bot.send_message(message.chat.id, "Выберите действие", reply_markup=markup)

@bot.message_handler(commands=["hello"])
def hello(message):
    bot.send_message(message.chat.id, "Привет")


@bot.message_handler(content_types=['text'])
def randomize(message):
    if message.text == "Рандомное число":
        num = random.randint(1, 100)
        bot.send_message(message.chat.id, num)
    if message.text == "Рандомный напиток":
        drinks = ["Энергетик", "Чай", "Кофе", "Сок", "Кола"]
        random_drink = random.choice(drinks)
        bot.send_message(message.chat.id, random_drink)
    if message.text == "Рандомный стикер":
        sticker = random.choice(["CAACAgIAAxkBAAJny2V7RWO-ie2wbcOw2a4nMHYRgqNiAAITFAACLmShSH7reYUGQrCuMwQ", "CAACAgIAAxkBAAJn02V7Rdapn5hF4dbsiLOKlCM2I14hAAIELQACPORZSStvIDgBJmKxMwQ", "CAACAgIAAxkBAAJnzWV7Rbl8oGyoYN2a3yXIyI-jTBW-AALWIQACXVzwSofXzTTMp-R_MwQ"])
        bot.send_sticker(message.chat.id, sticker)

bot.polling(none_stop=True)