import os
import telebot
from telebot import types

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

# /start
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id

    # Inline кнопка на сайт
    inline = types.InlineKeyboardMarkup()
    btn_site = types.InlineKeyboardButton(text='Поисковик', url='https://google.com')
    inline.add(btn_site)
    bot.send_message(chat_id, "По кнопке ниже можно перейти на сайт Google:", reply_markup=inline)

    # Выбор языка
    markup_lang = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_ru = types.KeyboardButton("ru Русский")
    btn_gb = types.KeyboardButton("gb English")
    markup_lang.add(btn_ru, btn_gb)
    bot.send_message(chat_id, "Выберите язык / Choose your language:", reply_markup=markup_lang)

# Обработка текста
@bot.message_handler(content_types=['text'])
def handle_text(message):
    chat_id = message.chat.id
    text = message.text

    # Выбор языка
    if text == "ru Русский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_hello = types.KeyboardButton("Поздороваться")
        btn_exit = types.KeyboardButton("Выйти")
        markup.add(btn_hello, btn_exit)
        bot.send_message(chat_id, "Вы выбрали русский язык 🇷🇺\nНажмите кнопку ниже:", reply_markup=markup)

    elif text == "gb English":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_hello = types.KeyboardButton("Greet")
        btn_exit = types.KeyboardButton("Exit")
        markup.add(btn_hello, btn_exit)
        bot.send_message(chat_id, "You chose English 🇬🇧\nPress a button below:", reply_markup=markup)

    # Поздороваться
    elif text in ["Поздороваться", "Greet"]:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Как стать автором на Хабре?")
        btn2 = types.KeyboardButton("Правила сайта")
        btn3 = types.KeyboardButton("Советы по оформлению публикации")
        btn_exit = types.KeyboardButton("Выйти")  # добавляем кнопку выхода
        markup.add(btn1, btn2, btn3, btn_exit)
        bot.send_message(chat_id, "Задайте интересующий вопрос:", reply_markup=markup)

    # FAQ ответы
    elif text == "Как стать автором на Хабре?":
        bot.send_message(chat_id, "Вы можете начать здесь: [ссылка](https://habr.com/ru/sandbox/start/)", parse_mode="MarkdownV2")
    elif text == "Правила сайта":
        bot.send_message(chat_id, "Прочитать правила сайта: [ссылка](https://habr.com/ru/docs/help/rules/)", parse_mode="MarkdownV2")
    elif text == "Советы по оформлению публикации":
        bot.send_message(chat_id, "Полезная информация: [ссылка](https://habr.com/ru/docs/companies/design/)", parse_mode="MarkdownV2")

    # Выход
    elif text in ["Выйти", "Exit"]:
        bot.send_message(chat_id, "Спасибо! Выход из бота.", reply_markup=types.ReplyKeyboardRemove())

# Запуск бота
bot.polling(none_stop=True)
