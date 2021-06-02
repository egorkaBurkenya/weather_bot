import telebot
from telebot import types

from weather import get_today_weather
from config import token

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def send_welcome_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('/weather')
    markup.add(button)
    bot.send_message(message.chat.id, "Добро пожаловать в моего тестового бота!🔮\n\n \
        Я использую его для теста разного функционала\
        \n\nСкорее всего ты видишь клавиатуру, попробуй нажать на нее", reply_markup=markup)

@bot.message_handler(commands=["weather"])
def send_today_weather(message):
    weather = get_today_weather()
    bot.send_message(message.chat.id, weather)

bot.polling()