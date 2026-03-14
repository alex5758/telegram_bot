import telebot
from telebot import types
bot = telebot.TeleBot('8627447114:AAG8j7OIC70fx3mm1zc5RmMOarWSbfxaN9U')
@bot.message_handler(commands = ['start'])
def url(message):
	markup = types.InlineKeyboardMarkup()
	btn1 = types.InlineKeyboardButton(text = 'Наш сайт', url = 'https://habr.com/ru/all/')
	markup.add(btn1)
	bot.send_message(message.from_user.id, "По кнопке ниже можно перейти на сайт хабра", reply_markup = markup)


@bot.message_handler(commands = ['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
	btn1 = types.KeyboardButton("ru Русский")
	btn2 = types.KeyboardButton("gb English")
	markup.add(btn1, btn2)
	bot.send_message(message.from_user.id, "ru Выберете язык / gb Choose your language", reply_markup = markup)
@bot.message_handler(commands = ['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
	btn1 = types.KeyboardButton("Поздороваться")
	markup.add(btn1)
	bot.send_message(message.from_user.id, "Привет! Я твой бот-помощник!", reply_markup = markup)

@bot.message_handler(content_types = ['text'])
def get_text_messages(message):
	if message.text == 'Поздороваться':
		markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
		btn1 = types.KeyboardButton('Как стать автором на Хабре?')
		btn2 = types.KeyboardButton('Правила сайта')
		btn3 = types.KeyboardButton('Советы по оформлению публикации')
		markup.add(btn1, btn2, btn3)
		bot.send_message(message.from_user.id, 'Задайте интересующий вопрос', reply_markup = markup)
	elif message.text == 'Как стать автором на Хабре?':
		bot.send_message(message.from_user.id, 'Вы пишите пост, его ' + '[ссылке](https://habr.com/ru/sandbox/start/)', parse_mode = 'Markdown')
	elif message.text == 'Правила сайта':
		bot.send_message(message.from_user.id, 'Прочитать правила сайта ' + '[ссылке](https://habr.com/ru/docs/help/rules/)', parse_mode = 'Markdown')
	elif message.text == 'Советы по оформлению публикации':
		bot.send_message(message.from_user.id, 'Подробно' + '[ссылке](https://habr.com/ru/docs/companies/design/)', parse_mode = 'Markdown')
bot.polling(none_stop = True, interval = 0)
		





