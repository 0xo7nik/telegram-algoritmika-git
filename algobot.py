import telebot
import json
users = dict()

def get_token():
    token = ''
    with open('token.json') as file:
        json_answer = json.load(file)
        token = json_answer['config']
    return token

token = get_token()
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start", "help"])
def send_start(message):
    if message.text.lower() == "/start":
        bot.send_message(message.from_user.id, "Привет! Я могу помочь тебе с любым математическим выражением.")
        if message.from_user.id in users.keys():
            bot.send_message(message.from_user.id, "Ты уже смешарик")
        users[message.from_user.id] = {
            'action': 'start',
            'data': []
        }
    if message.text.lower() == "/help":
        bot.send_message(message.from_user.id, "Напиши выражение, которое надо решить")

@bot.message_handler(content_types=['text'])
def send_answer(message):
    if message.text.lower():
        bot.send_message(message.from_user.id, eval(message.text))

bot.polling(none_stop=True, interval=0, timeout=120)