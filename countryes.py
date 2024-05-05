import telebot
from telebot import types
import datetime
import time

token = '6688742498:AAGViGNTVtwfAVUUqsVKC7VhRt0ww0mdREg'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
	global eu
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn12 = types.KeyboardButton('Давай начнем')
	markup.add(btn12)
	bot.send_message(message.from_user.id, "Привет это бот для игры в страны.Просто называй в любом порядке",reply_markup=markup)
	eu = ["Австрия",
"Албания",
"Андорра",
"Беларусь",
"Бельгия",
"Болгария",
"Босния и Герцеговина",
"Ватикан",
"Великобритания",
"Венгрия",
"Германия",
"Греция",
"Дания",
"Ирландия",
"Исландия",
"Испания",
"Италия",
"Кипр",
"Литва",
"Латвия",
"Лихтенштейн",
"Люксембург",
"Северная македония",
"Монако",
"Молдавия",
"Мальта",
"Нидерланды",
"Норвегия",
"Польша",
"Португалия",
"Россия",
"Румыния",
"Сан-Марино",
"Словакия",
"Словения",
"Сербия",
"Финляндия",
"Франция",
"Хорватия",
"Чехия",
"Черногория",
"Швейцария",
"Швеция",
"Эстония",
"Украина"]


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	global eu
	if message.text == 'Давай начнем':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn4 = types.KeyboardButton('Европа')
		btn3 = types.KeyboardButton('Азия(в разработке)')
		btn2 = types.KeyboardButton('Африка(в разработке)')
		btn1 = types.KeyboardButton('Америка(в разработке)')
		btn0 = types.KeyboardButton('Океания(в разработке)')
		markup.add(btn4, btn3, btn2, btn1, btn0)
		bot.send_message(message.from_user.id, 'Выберите режим', reply_markup=markup)
	if message.text == "Европа":
		global score
		score = 0
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		bot.send_message(message.from_user.id, 'хорошо, начнем игру. называйте страны', reply_markup=markup)
	if message.text in eu:
		score2 =score + 1
		print(score2)
		eu.remove(message.text)
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		bot.send_message(message.from_user.id, 'Да,' + " " + message.text + " - это европейская страна", reply_markup=markup)
		bot.send_message(message.from_user.id, score2, reply_markup=markup)


bot.polling(none_stop=True, interval=0)
