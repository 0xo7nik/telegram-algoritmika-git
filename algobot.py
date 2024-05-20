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
    if message.text.lower() == "/start":
        bot.send_message(message.from_user.id, "Привет! Я могу помочь тебе посчитать площадь треугольника по команде /area, а также могу посчитать любое математическое выражение по команде /maths.")
        users[message.from_user.id] = {
            'action': 'start',
            'data': []
        }
    if message.text.lower() == "/triangle_area":
        length = bot.send_message(message.from_user.id, "Длина основания треугольника?")
        bot.register_next_step_handler(length, get_length)
    if message.text.lower() == "/maths":
        maths = bot.send_message(message.from_user.id, "Напиши любое выражение")
        bot.register_next_step_handler(maths, get_maths)
    if message.text.lower() == "/circle_area":
        radius = bot.send_message(message.from_user.id, "Радиус окружности?")
        bot.register_next_step_handler(radius, get_radius)
    
#triangle_area
def get_length(message):
    global length, height
    length = int(message.text)
    height = bot.send_message(message.from_user.id, "Высота треугольника?")
    bot.register_next_step_handler(height, send_answer)
def send_answer(message):
    global length, height
    height = int(message.text)
    bot.send_message(message.from_user.id, f"Площадь треугольника равна: {(height*length)/2}")

#maths
def get_maths(message):
    global maths
    maths = message.text
    bot.send_message(message.from_user.id, eval(message.text))

#circle_area
def get_radius(message):
    global radius
    radius = int(message.text)
    bot.send_message(message.from_user.id, f"Площадь круга равна: {math.pi*(radius*radius)}")

bot.polling(none_stop=True, interval=0, timeout=120)