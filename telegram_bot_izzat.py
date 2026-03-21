import os
import telebot
from telebot import types
bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))
@bot.message_handler(commands = ['start'])
def url(message):
	markup = types.InlineKeyboardMarkup()
	btn1 = types.InlineKeyboardButton(text = 'the website', url = 'website2-production-b437.up.railway.app')
	markup.add(btn1)
	bot.send_message(message.from_user.id, "by clicking you can go to the website", reply_markup = markup)
@bot.message_handler(commands = ['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
	btn1 = types.KeyboardButton("english")
	markup.add(btn1)
	bot.send_message(message.from_user.id, "Choose your language", reply_markup = markup)
@bot.message_handler(commands = ['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
	btn1 = types.KeyboardButton("greeting")
	markup.add(btn1)
	bot.send_message(message.from_user.id, "hi im your bot helper", reply_markup = markup)
@bot.message_handler(content_types = ['text'])
def get_text_messages(message):
	if message.text == 'greeting':
		markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
		btn1 = types.KeyboardButton('website 1')
		btn2 = types.KeyboardButton('website 2')
		btn3 = types.KeyboardButton('website 3')
		markup.add(btn1, btn2, btn3)
		bot.send_message(message.from_user.id, 'please click to your website in which you are intersted', reply_markup = markup)
	elif message.text == 'website 1':
		bot.send_message(message.from_user.id, 'the search engine google ' + '[ссылке](https://google.com)', parse_mode = 'Markdown')
	elif message.text == 'website 2':
		bot.send_message(message.from_user.id, 'the social media ' + '[ссылке](https://facebook.com)', parse_mode = 'Markdown')
	elif message.text == 'website 3':
		bot.send_message(message.from_user.id, 'the encyclopedia' + '[ссылке](https://wikipedia.org)', parse_mode = 'Markdown')
bot.polling(none_stop = True, interval = 0)
