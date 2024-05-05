import time

import telebot
from telebot import types
# import time

token = '6854960054:AAHq0zl9CDWVrvoQv69VBjMq-q13cbow7Y0'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn4 = types.KeyboardButton('Здравствуйте')
    markup.add(btn4)
    bot.send_message(message.from_user.id, "Здравствуйте", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Здравствуйте':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.from_user.id, 'пришлите ФИО, посмотрю по возможности и напишу', reply_markup=markup)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.from_user.id, 'думаю стоит продолжить систематические перевязки, уход за аппаратом', reply_markup=markup)
        time.sleep(10)
        bot.send_message(message.from_user.id, 'аппарат сохранять 6 недель, Р-контроль через 1 мес. с осмотром', reply_markup=markup)
        time.sleep(60)
        bot.send_message(message.from_user.id, 'возможно продолжить в филлиале', reply_markup=markup)


bot.polling(none_stop=True, interval=0)
