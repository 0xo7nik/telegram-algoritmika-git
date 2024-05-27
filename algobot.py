import telebot
import json
import math


users = dict()

#token
def get_token():
    token = ''
    with open('token.json') as file:
        json_answer = json.load(file)
        token = json_answer['config']
    return token

token = get_token()
bot = telebot.TeleBot(token)
length, height = 0, 0
@bot.message_handler(commands=["start", "maths", "triangle_area", "circle_area"])
def send_start(message):
    def get_length(message):
        global length, height
        length = int(message.text)
        if message.text:
            height = bot.send_message(message.from_user.id, "Высота треугольника?")
            bot.register_next_step_handler(height, send_answer)
        else:
            bot.send_message(message.from_user.id, "Я тебя не понимаю.")
            
    def send_answer(message):
        global length, height
        height = int(message.text)
        if message.text:
            bot.send_message(message.from_user.id, f"Площадь треугольника равна: {(height*length)/2}")
        else:
            bot.send_message(message.from_user.id, "Я тебя не понимаю.")

    def get_maths(message):
        global maths
        maths = message.text
        if message.text:
            bot.send_message(message.from_user.id, f"Ответ: {eval(message.text)}")
        else:
            bot.send_message(message.from_user.id, "Я тебя не понимаю.")

    def get_radius(message):
        global radius
        radius = int(message.text)
        if message.text == radius:
            bot.send_message(message.from_user.id, f"Площадь круга равна: {math.pi*(int(message.text)**2)}")
        else:
            bot.send_message(message.from_user.id, "Я тебя не понимаю.")

    if message.text.lower() == "/start":
        bot.send_message(message.from_user.id, "Привет! Я могу помочь тебе посчитать площадь треугольника по команде /triangle_area, посчитать любое математическое выражение по команде /maths, а также посчитать площадь круга по команде /circle_area.")
        users[message.from_user.id] = {
            'action': 'start',
            'data': []
        }
    elif message.text.lower() == "/triangle_area":
        length = bot.send_message(message.from_user.id, "Длина основания треугольника?")
        bot.register_next_step_handler(length, get_length)

    elif message.text.lower() == "/maths":
        maths = bot.send_message(message.from_user.id, "Напиши любое выражение")
        if int(message.text):
            bot.register_next_step_handler(maths, get_maths)
        else:
            bot.send_message(message.from_user.id, "Я тебя не понимаю.")

    elif message.text.lower() == "/circle_area":
        radius = bot.send_message(message.from_user.id, "Радиус окружности?")
        bot.register_next_step_handler(radius, get_radius)

@bot.message_handler(content_types=["text"])
def send_text(message):
    if message.text:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Все мои команды указаны в /start.")
bot.polling(none_stop=True, interval=0, timeout=120)