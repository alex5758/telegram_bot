import os
import telebot
from telebot import types

# Берем токен из переменной окружения
bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id

    # 1️⃣ Inline-кнопка на сайт
    inline = types.InlineKeyboardMarkup()
    btn_site = types.InlineKeyboardButton(text='Наш сайт', url='https://habr.com/ru/all/')
    inline.add(btn_site)
    bot.send_message(chat_id, "По кнопке ниже можно перейти на сайт Хабра:", reply_markup=inline)

    # 2️⃣ Выбор языка через ReplyKeyboard
    markup_lang = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_ru = types.KeyboardButton("ru Русский")
    btn_gb = types.KeyboardButton("gb English")
    markup_lang.add(btn_ru, btn_gb)
    bot.send_message(chat_id, "Выберите язык / Choose your language:", reply_markup=markup_lang)

# Обработка текстовых сообщений
@bot.message_handler(content_types=['text'])
def handle_text(message):
    chat_id = message.chat.id
    text = message.text

    # Выбор языка
    if text == "ru Русский":
        bot.send_message(chat_id, "Вы выбрали русский язык 🇷🇺")
    elif text == "gb English":
        bot.send_message(chat_id, "You chose English 🇬🇧")

    # Поздороваться
    elif text == "Поздороваться":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Как стать автором на Хабре?")
        btn2 = types.KeyboardButton("Правила сайта")
        btn3 = types.KeyboardButton("Советы по оформлению публикации")
        markup.add(btn1, btn2, btn3)
        bot.send_message(chat_id, "Задайте интересующий вопрос:", reply_markup=markup)

    # Ответы на вопросы
    elif text == "Как стать автором на Хабре?":
        bot.send_message(chat_id, "Вы можете начать здесь: [ссылка](https://habr.com/ru/sandbox/start/)", parse_mode="MarkdownV2")
    elif text == "Правила сайта":
        bot.send_message(chat_id, "Прочитать правила сайта: [ссылка](https://habr.com/ru/docs/help/rules/)", parse_mode="MarkdownV2")
    elif text == "Советы по оформлению публикации":
        bot.send_message(chat_id, "Полезная информация: [ссылка](https://habr.com/ru/docs/companies/design/)", parse_mode="MarkdownV2")

# Запуск бота
bot.polling(none_stop=True, interval=0)
